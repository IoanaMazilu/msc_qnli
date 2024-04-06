# Premise: Sam had 98.0 pennies in his bank and he spent 93.0 of his pennies.
# Hypothesis: He has 5.0 pennies now.
# Golden Label: entailment

pennies_initial_premise = 98.0
pennies_spent_premise = 93.0
pennies_now_hypothesis = 5.0

# the hypothesis states the number of pennies Sam has now, which can be computed from the premise
# calculate the number of pennies Sam has now according to the premise
pennies_now_premise = pennies_initial_premise - pennies_spent_premise
if pennies_now_hypothesis != pennies_now_premise:
    # check if the number of pennies now in the hypothesis contradicts the number calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

