use JSON;
use XML::Simple;
my $file = $ARGV[0];

#system ("blastall -i query -d xm.fa -p blastp -e 1e-5 -m 7 >output.txt");
# Create the object of XML Simple
my $xmlSimple = new XML::Simple(KeepRoot   => 1);

# Load the xml file in object
my $dataXML = $xmlSimple->XMLin($file);

&fix_iterations($dataXML);


my $object =  $dataXML->{BlastOutput};

# use encode json function to convert xml object in json.
my $jsonString = encode_json($object);
# finally print json
print $jsonString;








sub fix_iterations {
my ($dataXML) = @_;
my $iterations = $dataXML->{BlastOutput}{BlastOutput_iterations}{Iteration};
  if(ref($iterations) eq 'HASH'){
    $dataXML->{BlastOutput}{BlastOutput_iterations}{Iteration} = [$dataXML->{BlastOutput}{BlastOutput_iterations}{Iteration}];
  }

my $iterations = $dataXML->{BlastOutput}{BlastOutput_iterations}{Iteration};


foreach my $iteration (@$iterations){

    my $hits = $iteration->{Iteration_hits}{Hit};
   foreach my $hit (@$hits){
      &fix_hsp($hit);
     }
}
}



sub fix_hsp {
my ($hit) = @_;

  my $hsp = $hit->{Hit_hsps}{Hsp};
  if(ref($hsp) eq 'HASH'){
	  $hit->{Hit_hsps}{Hsp}=[$hit->{Hit_hsps}{Hsp}];
  } 
}


