pennies_premise = 98.0
found_pennies = 93.0
total_pennies = pennies_premise + found_pennies

# the hypothesis refers to the total number of pennies Sam has now
if total_pennies!= 191.0:
    # check if the total number of pennies in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the total number of pennies in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
