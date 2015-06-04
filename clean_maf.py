#!/usr/bin/python3
# Copyright 2015 Telma G. Laurentino <telma.laurentino@gmail.com>
# This file is part of clean_maf.
# clean_maf is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# clean_maf is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with clean_maf. If not, see <http://www.gnu.org/licenses/>.

'''a script to correct deficient vcftools filtering of minimum allele frequency (maf) loci. input is a vcf file and in the output lines with maf lower than the specified are discarded'''

def parsar_vcf(vcf,  maf):
    vcf_handle = open(vcf,  "r")
    output = open (vcf+".clean_maf",  "w")
    count = 0
    for line in vcf_handle:
       
        if line.startswith("#"):
            output.write(line)
        else:
            lines= line.split()
            lines = "".join(lines[9:])
            zeros = lines.count("0")
            ones = lines.count("1")
            if ones/zeros >= float(maf): 
                output.write(line)
                count +=1
    output.close()
    vcf_handle.close()
    return count
    
  
if __name__ == "__main__":
    # usage: python3 clean_maf.py input.vcf maf_value(example: 0.05)
    from sys import argv
    vcf = argv[1]
    maf = argv[2]
    print(parsar_vcf(vcf,  maf))  # prints how many lines survive the cleaning


