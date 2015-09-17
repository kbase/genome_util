use strict;
use Data::Dumper;
use JSON;
use Bio::KBase::workspace::Client;
use Bio::KBase::AuthToken;
my $ws_id="pranjan77:1436286867421";
my $ws_url = "https://ci.kbase.us/services/ws";
my $token  = $ENV{KB_AUTH_TOKEN};
if (!$token){
my $to = Bio::KBase::AuthToken->new();
$token = $to->{token};
}
my $file = $ARGV[0];
my $id = $ARGV[1];
open (FILE, $file) or die ("nnc");

my $ws_doc1 = from_json(join ("", <FILE>));

my $ws_doc=$ws_doc1;

my $wsc = Bio::KBase::workspace::Client->new($ws_url, token=>$token );




my $metadata = $wsc->save_object({id =>$id, type =>"KBaseGwasData.BlastOutput", data => $ws_doc, workspace => $ws_id});
