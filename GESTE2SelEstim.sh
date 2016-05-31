#!/bin/bash
#co-authory Telma G. Laurentino(Telpidus); Francisco Pina-Martins(StuntsPT)
#usage: bash script.sh <inputfile.geste> <#loci> <#pops> <output_file>

# Make sure script exists on error (we're using "rm" here)
set -e

# Get the allele frequencies from GESTE and write them in SelEstim format
touch full_data_dump
for i in $(seq 1 $3);
  do
    grep "\[pop\]\=${i}$" -A $2 $1 |cut -f 4,5 |tail -n +2 > new_data_dump
    paste full_data_dump new_data_dump > old_data_dump
    mv old_data_dump full_data_dump
  done

# Write the header
echo $3 > tmpfile
echo $2 >> tmpfile

# Write the data
cat tmpfile full_data_dump | sed 's/\t/ /g' |sed 's/ \+/ /g' | sed 's/^ //g' > $4

# Clean-up
rm tmpfile
rm new_data_dump
rm full_data_dump
