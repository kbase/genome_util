

typedef structure {
  float Parameters_expect;
  string Parameters_filter;
  int Parameters_gap-extend;
  int Parameters_gap-open;
  string Parameters_matrix;
}Parameters;



typedef structure {
  Parameters Parameters;
} BlastOutput_param;




typedef structure {
  int Hsp_align-len;
  float Hsp_bit-score;
  float Hsp_evalue;
  int Hsp_hit-frame;
  int Hsp_hit-from;
  int Hsp_hit-to;
  string Hsp_hseq;
  int Hsp_identity;
  string Hsp_midline;
  int Hsp_num;
  int Hsp_positive;
  string Hsp_qseq;
  int Hsp_query-frame;
  int Hsp_query-from;
  int Hsp_query-to;
  int Hsp_score;
}Hsp;



typedef structure {
  Hsp Hsp;
}Hit_hsps



typedef structure {
  string Hit_accession;
  string Hit_def;
  string Hit_id;
  int Hit_len;
  int Hit_num;
  Hit_hsps Hit_hsps;
}hit_details;

list <hit_details> Hit;

typedef structure {
  Hit Hit;
}


typedef structure {
    Hit Hit;
    string Iteration_iter-num;
    string Iteration_query-ID;
    string Iteration_query-def;
    string Iteration_query-len;
}Iteration_hits;


typedef structure {
 Iteration_hits Iteration_hits;
}Iteration;





typedef structure {
  string BlastOutput_db;
  string BlastOutput_program;
  string BlastOutput_query-ID;
  string BlastOutput_query-def;
  string BlastOutput_query-len;
  string BlastOutput_reference;
  string BlastOutput_version;
  BlastOutput_param BlastOutput_param;
  BlastOutput_iterations BlastOutput_iterations;
}BlastOutput;


