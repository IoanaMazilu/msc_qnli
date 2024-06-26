pennies_initial_premise = 98.0
pennies_spent_premise = 93.0
pennies_now_hypothesis = 0.0

# the hypothesis refers to the number of pennies Sam has now, which can be computed from the premise
# compute the number of pennies Sam has now according to the premise
pennies_now_premise = pennies_initial_premise - pennies_spent_premise
if pennies_now_hypothesis!= pennies_now_premise:
    # check if the number of pennies in the hypothesis contradicts the number of pennies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
