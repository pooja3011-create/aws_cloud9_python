# -*- coding: utf-8 -*-

"""
TODO: add docstring
"""
import logging
import re
import json

# name of the file to be read
fname = "preproinsulin-seq.txt"
structure_fname = "insulin_structure.json"
file_suffix = "-seq-clean.txt"
amino_acid_weights_fname = "amino_acid_weights.json"

# logging information
FORMAT = '%(levelname)-8s | %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

pattern = r"^[0-9]*([a-z\s]*)$"

# lists to contain the information
clean_lines = list()
sequences = list()


# get the insulin structure. Array of objects
# - name: string, name of the section, becomes the file prefix
# - start: int, starting index in the sequence (1-based)
# - end: int, ending index in the sequence (1-based)
with open(structure_fname, "rt") as sfile:
    insulin_structure = json.load(sfile)


# read the amino acid weights
# - "<char>" : weight
# - character : float
with open(amino_acid_weights_fname, "rt") as aa_weights_file:
    amino_acid_weights = json.load(aa_weights_file)


# parse the insulin file
with open(fname, "rt") as insulin_file:
    for line_number, line in enumerate(insulin_file):
        logging.debug(f"::: working on line {line_number}")
        
        # remove the whitespace
        line = line.strip()
        
        # exclude the non-data part
        if line.startswith("ORIGIN"):
            logging.debug("ORIGIN line is found. Excluding it from the clean data")
            continue
        
        if line.startswith("//"):
            logging.debug("// line is found. Excluding it from the clean data")
            continue
    
        # parse the data
        match = re.match(pattern, line)
        if match is  None:
            logging.error(f"Could not find a regex on line {line_number}")
            continue
    
        # extract the match
        logging.debug(f"::: Parsed the following sequence on line: {line_number}")
        parsed_sequence = match.groups()[0].strip()
        logging.debug(parsed_sequence)
        
        # save the parsed sequence
        current_sequences = parsed_sequence.split(" ")
        sequences.extend(current_sequences)

logging.info(f"Finished processing the file {fname}")

# merge everthing into a single string
sequence_string = "".join(sequences)

# sanity check
assert len(sequence_string) == 110
logging.info("Successfully parsed the DNA sequence")

logging.debug(sequences)
logging.debug(sequence_string)

molecule = dict()

# post processing
for section in insulin_structure:
    name = section["name"]
    start = int(section["start"])-1
    end = int(section["end"])-1
    subsection = sequence_string[start : end+1]

    out_fname = f"{name}{file_suffix}"
    with open(out_fname, "wt") as out_file:
        out_file.write(subsection)
    logging.info(f"wrote {len(subsection)} characters to the file: {out_fname}")
    logging.debug(subsection)
    
    molecule[name] = subsection


# construct insulin molecule
insulin = molecule["ainsulin"] + molecule["binsulin"]
 

characters_found = sorted(set(insulin))

# fill the dictionary
amino_acid_counts = dict()
for character in characters_found:
    amino_acid_counts[character] = insulin.count(character)

weight_sum = 0.0
for character in characters_found:
    weight = amino_acid_weights[character.upper()]
    weight_sum += amino_acid_counts[character] * weight

real_molecular_weight = 5807.63
percent_error = (weight_sum - real_molecular_weight) / real_molecular_weight * 100.
print(f"Percent error: {percent_error}")

pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

seqCount = {x: float(insulin.count(x)) for x in pKR.keys() }
print(seqCount)

ph = 0.0
while ph <= 14:
    in_charges = list()
    for x in ['k','h','r']:
        value = pKR[x]
        result = seqCount[x] * (10**value) / (10**ph + 10**value)
        in_charges.append(result)
    
    out_charges = list()
    for x in  ['y','c','d','e']:
        value = pKR[x]
        result = seqCount[x] * (10**ph) / (10**ph + 10**pKR[x])
        out_charges.append(result)
    
    sum_in = sum(in_charges)
    sum_out = sum(out_charges)
    net_charge = sum_in - sum_out
    
    print('{0:.2f}'.format(ph), net_charge)
    ph += 1.0
    