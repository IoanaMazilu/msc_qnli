us_bonds_purchased_premise = 7500
us_bonds_purchased_hypothesis = 3500

# the hypothesis refers to the value of US saving bonds purchased by Robert, which is also mentioned in the premise
if us_bonds_purchased_hypothesis >= us_bonds_purchased_premise:
    # check if the value in the hypothesis contradicts the estimate of 'less than us_bonds_purchased_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of the bonds
    # any value less than 'us_bonds_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
