#!/bin/bash
# co-authory Telma G. Laurentino(Telpidus); Francisco Pina-Martins(StuntsPT)
# Usage: bash GESTE2selestim.sh <inputfile.geste> <outputfile.selestim>

# Make sure script exits on error (we're using "rm" here)
set -e

# Get the number of loci from the GESTE file
loci=$(head -n 1 ${1} | sed 's/.*=//')

# Get the number of populations from the GESTE file
pops=$(head -n 3 ${1} | tail -n 1 |sed 's/.*=//')

# Get the allele frequencies from GESTE and write them in SelEstim format
touch full_data_dump
for i in $(seq 1 ${pops});
  do
    grep "\[pop\]\=${i}$" -A ${loci} ${1} |cut -f 4,5 |tail -n +2 > new_data_dump
    paste full_data_dump new_data_dump > old_data_dump
    mv old_data_dump full_data_dump
  done

# Write the header
echo ${pops} > tmpfile
echo ${loci} >> tmpfile

# Write the data
cat tmpfile full_data_dump | sed 's/\t/ /g' |sed 's/ \+/ /g' | sed 's/^ //g' > ${2}

# Clean-up
rm tmpfile
rm new_data_dump
rm full_data_dump
