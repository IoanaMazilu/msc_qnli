us_saving_bonds_premise = 1500
us_saving_bonds_hypothesis = 7500

# the hypothesis talks about the value of US saving bonds purchased by Robert, referenced also in the premise
if us_saving_bonds_hypothesis <= us_saving_bonds_premise:
    # check if the hypothesis value contradicts the estimate of 'us_saving_bonds_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of US saving bonds
    # any value greater than 'us_saving_bonds_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
