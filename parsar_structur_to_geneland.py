#!/usr/bin/python3

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
