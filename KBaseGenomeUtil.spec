module KBaseGenomeUtil {

    /* @id ws KBaseGenomeUtil.BlastOutput */
    typedef string blast_output_ref;

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

    typedef structure {
    	string gene_id;			/*gene_id is a KBase feature id*/
    	float e-value;			/*BLAST input parameters*/
	float identity;			/*BLAST input parameters*/
	float score;			/*BLAST input parameters*/
    
    } hit;
    typedef list<hit> hits;



    /* description of method and parameters */
    funcdef blast_against_genome(BlastGenomeParams params) 
      			returns (blast_output_ref) authentication required;



    /* reference of compare_genome_groups output object */
    typedef string compare_genome_groups_output_ref;



	/* Input parameters for compare_genome_groups function.

	   compare_genome_id -  ID of the compare_genome object used as input.
	   compare_genome_ws -  workspace ID the compare_genome object used as input.
	   genomes -  list of genomes in the pan genome from which compare_genome object is dervied
	   genome_workspaces - list of workspaces for genomes in the pan genome.
	   groups - list of groups for genomes in the pan genome object. 
	   output_id -  ID of the output object.

	 */



	typedef structure {
		string compare_genome_id;
		string compare_genome_ws;
		list<string> genomes;
		list<string> genome_workspaces;
		list <string> groups;
		string output_id;
	} compare_genome_groups_params;

	/* This function is used after running build_pangenome and compare_genomes functions. It takes 
	   a compare_genomes output (derived from pangenome object) as input. It also takes the broad groupings eg. rhizosphere, bulk-soil
	   for each genome. The output object is optimized for displaying comparison of groups.
	 */
	authentication required;
	funcdef compare_genome_groups(compare_genome_groups_params input) 
		returns (compare_genome_groups_output_ref);

};






