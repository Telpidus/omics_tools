#!/usr/bin/python3

# Copyright 2015 Telma G. Laurentino <telma.laurentino@gmail.com>
# This file is part of GESTE2BayEnv.
# GESTE2BayEnv is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GESTE2BayEnv is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GESTE2BayEnv. If not, see <http://www.gnu.org/licenses/>.

'''a script to create a BayEnv2.0 input from .GESTE files (typical BayScan input). If you have a .vcf file you can convert it to .GESTE with PGDSpider'''

infile= open("/home/telmagl/Desktop/BayEnv/bayenv2_64bit/BayEnv_noSE/Tlepidus_noSE_27_noLD.geste",  "r")

def parsar_geste(infile): #parsses the .geste file (Bayscan input)
    SNP= {} #dictionary with #SNP as key  = [frequencyAlelleA in pop_1, frequencyAlelleA in pop_2...], [frequencyAlelleB in pop_1, frequencyAlelleB in pop_2...]
    for line in infile:
        line = line.split()
        try:
            int(line[0]) #to ignore all the lines which do not correspond to SNP information
        except:
            continue
        if line[0] not in SNP:
            SNP [line[0]] = [[ ], [ ]]
        alelleA = line[3] #column from geste file with info on frequency of alelleA per pop
        alelleB = line[4]
        SNP[line[0]][0].append(alelleA) #frequency of alelleA in all pops
        SNP[line[0]][1].append(alelleB) #frequency of alelleB in all pops
    return SNP

SNP = parsar_geste(infile)

def write_SNPSFILE_and_SNPFILE(SNP, SNPSFILE): #creates the input files for BayEnv2.0
    outfile = open (SNPSFILE,  "w")
    for keys,  values in SNP.items():
        alelleA = "\t".join(values[0])
        alelleB = "\t".join(values [1])
        snp = alelleA + "\n" + alelleB + "\n"
        outfile.write (snp)
        SNPFILE = open ("/home/telmagl/Desktop/BayEnv/bayenv2_64bit/BayEnv_noSE/Inidivid_SNPS" + keys + ".txt",  "w") #writes the individual SNP files 
        SNPFILE.write(snp)
        SNPFILE.close()
    outfile.close()
    return SNPSFILE

write_SNPSFILE_and_SNPFILE(SNP, "/home/telmagl/Desktop/BayEnv/bayenv2_64bit/BayEnv_noSE/noSE_SNPSFILE_noLD") #writes de SNPSFILE with all SNPs info
    
    
    
