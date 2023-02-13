"""
Your module description
"""
import json

json_fname = "insulin.json"

def read_json_file(file_name):
    data = None
    try:
        with open(file_name) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Ops, something went wrong")
    return data


data = read_json_file(json_fname)

if data:
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")

# Calculating the molecular weight of insulin  
# Getting a list of the amino acid (AA) weights  
aaWeights = data['weights']
# Count the number of each amino acids  

aacids = ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']

aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in aacids})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))
print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))