#!/usr/bin/env python

# standard library imports
import os
import sys
import traceback
import argparse
import json
import logging
import time
import pprint 
from os import environ
from ConfigParser import ConfigParser

# 3rd party imports
import requests

# KBase imports
import biokbase.genome_util.script_util as script_util
from biokbase.genome_util.KBaseGenomeUtilImpl import KBaseGenomeUtil

DEPLOY = 'KB_DEPLOYMENT_CONFIG'
SERVICE = 'KB_SERVICE_NAME'
TOP = 'KB_TOP'
DEPLOYMENT = 'KB_TARGET'

# Note that the error fields do not match the 2.0 JSONRPC spec

def get_config_file(default = None):
    path = environ.get(DEPLOY, default)
    if path is None:
      cand = environ.get(DEPLOYMENT, None)
      if cand is None:
        cand = environ.get(TOP, None)
        if cand is None:
          return None
      return os.path.join(cand, 'deployment.cfg')
    else:
      return path


def get_service_name(default = None):
    return environ.get(SERVICE, default)


def get_config(module = None, cfg_path = None):
        
    if not get_config_file(cfg_path) or not get_service_name(module):
        return None
    retconfig = {}
    config = ConfigParser()
    config.read(get_config_file())
    for nameval in config.items(get_service_name()):
        retconfig[nameval[0]] = nameval[1]
    return retconfig



# TODO: Generalize the following to handle all modules and methods

def run_svc(service_url, module, command, param_file, token=None, level=logging.INFO, logger=None):
    """
    Narrative Job Service Genome util service wrapper.

    Args:
        ws_url: A url for the KBase workspace service.
        param_file: A file name for the input parameters.
        output_filename: A file name where the output JSON string should be stored.
        level: Logging level, defaults to logging.INFO.

    """

    if logger is None:
        logger = script_util.stderrlogger(__file__)

    if service_url != "impl":
        logger.error("Only 'impl' is accepted as svc_url")
        raise
        # TODO: 
        
    #TODO: Dynamically load required module, for now direct import
    config = get_config(module = module, cfg_path = None)
    if config is None:
        logger.error("Could not find deployment.cfg to configure the service\n\tPlease ensure {0},{1},or{2} to be defined".format(DEPLOY, DEPLOYMENT, TOP))
        raise
    gu_hndlr = KBaseGenomeUtil(config)
    with open(param_file) as paramh:
      param = json.load(paramh)

    if token is None:
        token = environ.get('KB_AUTH_TOKEN', None)
        logger.error("Could not retrieve user token from KB_AUTH_TOKEN")

    #TODO: May add full call ctx
    try:
        logger.info("Execute {0}.{1} with {2}".format(module,command, pprint.pformat(param)))
        output = getattr(gu_hndlr,command)({'token' : token },param)

        logger.info("Output: {0}".format(pprint.pformat(output)))
    
    except: 
        logger.exception("".join(traceback.format_exc()))
        sys.exit(1)

    return output


# called only if script is run from command line
if __name__ == "__main__":	
    import sys

    parser = argparse.ArgumentParser(prog='njs-run-genome-util.py', 
                                     description='NJS Service Wrapper Script',
                                     epilog='Authors: Shinjae Yoo')
    parser.add_argument('-s', '--service_url', help='Service url', action='store', type=str, default='impl', nargs='?', required=False)
    parser.add_argument('-w', '--ws_url', help='Workspace url', action='store', type=str, default='https://kbase.us/services/ws/', nargs='?', required=False)
    parser.add_argument('-m', '--module', help='Module name', action='store', type=str, default='KBaseGenomeUtil', nargs='?', required=False)
    parser.add_argument('-c','--command', help ='Command name', action='store', type=str, nargs='?', required=True)
    parser.add_argument('-p','--param_file', help ='Input parameter file name', action='store', type=str, nargs='?', required=True)
    parser.add_argument('-t','--token', help ='token', action='store', type=str, nargs='?', default=None, required=False)

    args = parser.parse_args()

    logger = script_util.stderrlogger(__file__)
    try:
        ret_json = run_svc(args.service_url, args.module, args.command, args.param_file, logger=logger)
        
        #logger.info("Writing out JSON.")
        #with open(args.output_filename, "w") as outFile:
        #    outFile.write(json.dumps(ret_json,sort_keys = True, indent = 4))
        
   	logger.info("Execution completed.")
    except:
        logger.exception("".join(traceback.format_exc()))
        sys.exit(1)
    
    sys.exit(0)
