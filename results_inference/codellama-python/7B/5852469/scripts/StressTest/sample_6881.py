saving_bonds_premise = 1500
saving_bonds_hypothesis = 7500

# the hypothesis refers to the number of saving bonds purchased by Robert
if saving_bonds_hypothesis <= saving_bonds_premise:
    # check if the estimate of'saving_bonds_hypothesis' contradicts the number of saving bonds purchased by Robert
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of saving bonds
    # any number of saving bonds greater than'saving_bonds_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
