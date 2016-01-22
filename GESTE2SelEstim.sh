#!/bin/bash
#co-authory Telma G. Laurentino(Telpidus); Francisco Pina-Martins(StuntsPT)
#usage: bash script.sh <inputfile.geste> <#loci> <#pops> <output_file>

set -e

echo $3 > tmpfile
echo $2 >> tmpfile
echo "<#indv*2 pop1> <#indv*2 pop2> <#indv*2 pop3> <...>" >> tmpfile


touch teste
for i in $(seq 1 $3); 
 do
 grep "\[pop\]\=$i" -A $2 $1 |cut -f 4,5 |paste teste - > teste$i 
 
done
paste teste* >> tmpfile
rm teste*

sed '4d' tmpfile |sed 's/	\+/ /g' | sed 's/ \+/ /g' | sed 's/^ //g' > $4

rm tmpfile





