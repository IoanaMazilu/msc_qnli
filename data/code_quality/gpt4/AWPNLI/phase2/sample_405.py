pennies_bank_premise = 98.0
pennies_found_premise = 93.0
total_pennies_hypothesis = 190.0

# the hypothesis refers to the total number of pennies, which are also mentioned in the premise
# compute the total number of pennies in the premise
total_pennies_premise = pennies_bank_premise + pennies_found_premise
if total_pennies_hypothesis != total_pennies_premise:
    # check if the total number of pennies in the hypothesis contradicts the total number of pennies from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
