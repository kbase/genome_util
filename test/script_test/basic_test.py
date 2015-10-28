# Test script for genome_util package - it should be launched from
# the root of the genome_util module, ideally just with 'make test', as
# it looks for a hardcoded relative path to find the 'test.cfg' file
import unittest
import json
import ConfigParser

from pprint import pprint

from subprocess import call

from biokbase.auth import Token

# Before all the tests, read the config file and get a user token and
# save it to a file used by the main service script
class TestGenomeUtilMethodsSetup(unittest.TestCase):
  def setUp(self):
    config = ConfigParser.RawConfigParser()
    config.read('test/test.cfg')
    user_id = config.get('GenomeUtilTest','user')
    password = config.get('GenomeUtilTest','password')
    token = Token(user_id=user_id, password=password)
    token_file = open('test/script_test/token.txt','w')
    token_file.write(token.token)

# Define all our other test cases here
class TestGenomeUtilMethods(TestGenomeUtilMethodsSetup):

  def test_method(self):
    print("\n\n----------- basic test ----------")

    # call the script with some input
    out = call(["run_KBaseGenomeUtil.sh", 
       "test/script_test/input.json", 
       "test/script_test/output.json", 
       "test/script_test/token.txt"])

    # print error code of implementation
    print(out);

    # read and print output of the function
    with open('test/script_test/output.json') as o:    
        output = json.load(o)
    pprint(output)


# start the tests if run as a script
if __name__ == '__main__':
    unittest.main()
