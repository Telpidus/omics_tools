#!/bin/bash
#co-authory Telma G. Laurentino(Telpidus); Francisco Pina-Martins(StuntsPT)
#usage: bash script.sh <inputfile.geste> <#loci> <#pops> <output_file>

# make sure script exists on error(careful with rm's)
set -e

# writes the header
echo $3 > tmpfile
echo $2 >> tmpfile
echo "<#indv*2 pop1> <#indv*2 pop2> <#indv*2 pop3> <...>" >> tmpfile # you have to input this by hand. sorry. 

# gets the alleles freqs. from geste file and writes into SelEstim format
touch teste
for i in $(seq 1 $3); 
 do
 grep "\[pop\]\=$i" -A $2 $1 |cut -f 4,5 |paste teste - > teste$i 
 
done
paste teste* >> tmpfile
rm teste*

sed '4d' tmpfile |sed 's/	\+/ /g' | sed 's/ \+/ /g' | sed 's/^ //g' > $4

rm tmpfile





