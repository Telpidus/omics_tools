#!/usr/bin/python3

# Copyright 2015 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of loci_pattern_seeker.
# loci_pattern_seeker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# loci_pattern_seeker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with loci_pattern_seeker.  If not, see <http://www.gnu.org/licenses/>.


from collections import OrderedDict

def genotype(line,  treshold):
    """Define the type of population pattern."""
    line = line.split()
    if int(line[1]) <= treshold and int(line[2]) <= treshold:
        pat = "H2"
    elif int(line[2]) <= treshold and int(line[3]) <= treshold:
        pat = "H1"
    else:
        pat = "mix"
    return pat


def parse_genepop_DIV(infile_name,  treshold):
    """Parses a GenePop .DIV file and returns a dict with the patterns."""
    wanted = 0
    infile = open(infile_name, 'r')
    patterns = OrderedDict()
    for lines in infile:
        if lines.startswith("Locus:") and wanted == 0:
            wanted = 1
            snp = lines.split()[-1]
        elif lines.startswith("Gal") and wanted == 1:
            galpat = genotype(lines, treshold)
        elif lines.startswith("Ger") and wanted == 1:
            gerpat = genotype(lines, treshold)
        elif lines.startswith("Esp") and wanted == 1:
            mtzpat = genotype(lines, treshold)
        elif lines.startswith("Total:") and wanted == 1:
            if (galpat == "H1" and gerpat == "H1" and mtzpat != "H1") or (galpat == "H2" and gerpat == "H2" and mtzpat != "H2"):
                patterns[snp] = "112"
            elif (galpat == "H1" and gerpat != "H1" and mtzpat == "H1") or (galpat == "H2" and gerpat != "H2" and mtzpat == "H2"):
                patterns[snp] = "121"
            elif (galpat == "H1" and gerpat != "H1" and mtzpat != "H1") or (galpat == "H2" and gerpat != "H2" and mtzpat != "H2"):
                patterns[snp] = "122"
            elif (galpat != "H1" and gerpat == "H1" and mtzpat == "H1") or (galpat != "H2" and gerpat == "H2" and mtzpat == "H2"):
                patterns[snp] = "211"
            elif (galpat != "H1" and gerpat == "H1" and mtzpat != "H1") or (galpat != "H2" and gerpat == "H2" and mtzpat != "H2"):
                patterns[snp] = "212"
            elif (galpat != "H1" and gerpat != "H1" and mtzpat == "H1") or (galpat != "H2" and gerpat != "H2" and mtzpat == "H2"):
                patterns[snp] = "221"
            else:
                patterns[snp] = "222"
            wanted = 0

    return patterns

if __name__ == "__main__":
    from sys import argv
    # Usage: python3 loci_pattern_seeker.py Genepop.DIV treshold
    patterns = parse_genepop_DIV(argv[1],  int(argv[2]))
    for k, v in patterns.items():
        print(k + " - " + v)
