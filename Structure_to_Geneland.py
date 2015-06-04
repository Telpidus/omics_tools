#!/usr/bin/python3

# Copyright 2015 Telma G. Laurentino <telma.laurentino@gmail.com>
# This file is part of parsar_structure_to_geneland.
# parsar_structure_to_geneland is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# parsar_structure_to_geneland is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with parsar_structure_to_geneland. If not, see <http://www.gnu.org/licenses/>.


def read_structure(docinput):
    '''parsses the structure file ans returns a dictionary with the two seqs per indiv {MnT6 : [[4, 2, 3,...] [...]]} '''
    handle = open(docinput,  "r")
    handle.readline()
    indiv_info = {}
    for lines in handle:
        lines = lines.split() 
        if lines[0] in indiv_info:
            indiv_info[lines[0]] += [lines[2:]]
        else: 
            indiv_info[lines[0]] = [lines[2:]]
    
    handle.close()    
    return indiv_info
    
    
def merge_indiv(indiv_info):
    '''uses the dictionary and merges the values to creat a genotype per indiv'''
    merged_indiv = {}
    for indiv in indiv_info:
        merged_indiv[indiv] =[]
        for i, j in zip(indiv_info[indiv][0], indiv_info[indiv][1]):
            merged_indiv[indiv].append(i+j)

    return merged_indiv


def write_genelandin(merged_indiv, outfile_name):
    '''creates the file ready to input in Geneland'''
    outfile = open(outfile_name,  "w")
    for indiv in merged_indiv:
        write_string = indiv + " " + " ".join(merged_indiv[indiv]) + "\n"
        write_string = write_string.replace("-9",  "9")
        outfile.write(write_string)
    
    
    outfile.close()


if __name__ == "__main__":
    
    aa = read_structure("/home/telmagl/Desktop/Tlepidus_noSE/Structure/Telpidus_noSE_structure_input")
    bb = merge_indiv(aa)
    write_genelandin(bb, "/home/telmagl/Desktop/Tlepidus_noSE/Structure/Telpidus_noSE_geneland_input")
