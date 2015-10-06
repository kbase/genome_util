module KBaseGenomeUtil {


    /*genome_id is a KBase genome object id*/
    typedef string genome_id;

    
    typedef structure {
    	
	/*only one parameter from query and gene_id is required*/
	string query;			/*user can paste gene sequence directly*/
	string gene_id; 		/*gene_id is a KBase feature id*/


    	list<genome_id> genome_ids; 	/*database to search against*/
    	string blast_program;		/*BLAST input parameters, blastp, blastn or etc.*/
    	float e-value;			/*BLAST input parameters*/
	float identity;			/*BLAST input parameters, sequence identity*/
	float score;			/*BLAST input parameters, blast summary score*/

    } BlastGenomeParams;



/*
@optional Parameters_matrix Parameters_sc-match Parameters_sc-mismatch

*/


typedef structure {
  string Parameters_expect;
  string Parameters_filter;
  string Parameters_gap-extend;
  string Parameters_gap-open;
  string Parameters_matrix;
  string Parameters_sc-match;
  string Parameters_sc-mismatch;
}Parameters;



typedef structure {
  Parameters Parameters;
} BlastOutput_param;


/*
 @optional Hsp_query-frame Hsp_hit-frame
*/


typedef structure {
  string Hsp_align-len;
  string Hsp_bit-score;
  string Hsp_evalue;
  string Hsp_hit-frame;
  string Hsp_hit-from;
  string Hsp_hit-to;
  string Hsp_hseq;
  string Hsp_identity;
  string Hsp_midline;
  string Hsp_num;
  string Hsp_positive;
  string Hsp_qseq;
  string Hsp_query-frame;
  string Hsp_query-from;
  string Hsp_query-to;
  string Hsp_score;
}Hsp_details;

typedef list <Hsp_details> Hsp;

typedef structure {
  Hsp Hsp;
}Hit_hsps;



typedef structure {
  string Hit_accession;
  string Hit_def;
  string Hit_id;
  string Hit_len;
  string Hit_num;
  Hit_hsps Hit_hsps;
}hit_details;



/*
@optional hit_details
*/
typedef list <hit_details> Hit;




/*
@optional Hit
*/
typedef structure {
    Hit Hit;
}Iteration_hits;


/*
@optional Iteration_hits Iteration_iter-num Iteration_query-ID Iteration_query-def Iteration_query-len
*/
typedef structure {
    Iteration_hits Iteration_hits;
    string Iteration_iter-num;
    string Iteration_query-ID;
    string Iteration_query-def;
    string Iteration_query-len;

}Iteration_details;

typedef list <Iteration_details> Iteration;

typedef structure {
 Iteration Iteration;
}BlastOutput_iterations;



/*
@optional err_msg BlastOutput_iterations BlastOutput_query-def BlastOutput_reference
*/

typedef structure {
  string BlastOutput_db;
  string BlastOutput_program;
  string BlastOutput_query-ID;
  string BlastOutput_query-def;
  string BlastOutput_query-len;
  string BlastOutput_reference;
  string BlastOutput_version;
  string err_msg;
  BlastOutput_param BlastOutput_param;
  BlastOutput_iterations BlastOutput_iterations;
}BlastOutput;



 /* description of method and parameters */
 funcdef blast_against_genome(BlastGenomeParams params) 
 	returns (BlastOutput) authentication required;

    /* 
        The workspace ID of a BlastOutput data object.
        @id ws BlastOutput
    */
    typedef string ws_blastoutput_id;

    /* 
        The workspace ID of a FeatureSet data object.
        @id ws KBaseCollections.FeatureSet
    */
    typedef string ws_featureset_id;

    typedef structure {
    	
	ws_blastoutput_id in_id;			/* The workspace input object id */
    	ws_featureset_id out_id;			/* The workspace output object id */
	string ws_id;					/* The workspace id */
        float evalue;                                   /* Evalue cut-off */
        int entries;                                   /* The number of entries to keep */

    } FilterBlastOutputParams;

    typedef structure {
    	ws_featureset_id obj_name;			/* WS object name */
    	string ws_id;			/* The workspace name */
    }FeatureSetOutput;

    /*  Filter BlastOutput object*/
    funcdef filter_BlastOutput(FilterBlastOutputParams params)
        returns (FeatureSetOutput) authentication required;


};






