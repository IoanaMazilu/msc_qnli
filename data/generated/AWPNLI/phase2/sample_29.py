# Premise: Sam had 98.0 pennies in his bank and he spent 93.0 of his pennies.
# Hypothesis: He has 0.0 pennies now.
# Golden Label: contradiction

initial_pennies_premise = 98.0
spent_pennies_premise = 93.0
remaining_pennies_hypothesis = 0.0

# the hypothesis refers to the number of pennies, which are also mentioned in the premise
# compute the remaining number of pennies in the premise
remaining_pennies_premise = initial_pennies_premise - spent_pennies_premise
if remaining_pennies_hypothesis != remaining_pennies_premise:
    # check if the number of remaining pennies in the hypothesis contradicts the number of remaining pennies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

