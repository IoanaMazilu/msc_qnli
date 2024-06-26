# the hypothesis refers to the number of bonds sold in a certain denomination, referenced also in the premise
if denomination_bonds_hypothesis <= 70:
    # check if the hypothesis value contradicts the estimate of 'denomination_bonds_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of bonds sold in a certain denomination
    # any number of bonds greater than 'denomination_bonds_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
