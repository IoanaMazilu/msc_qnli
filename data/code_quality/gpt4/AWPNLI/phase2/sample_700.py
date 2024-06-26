quarters_initial_premise = 49.0
quarters_spent_premise = 21.0
quarters_hypothesis = 28.0

# the hypothesis refers to the number of quarters, which are also mentioned in the premise
# compute the remaining number of quarters in the premise
quarters_remaining_premise = quarters_initial_premise - quarters_spent_premise
if quarters_hypothesis != quarters_remaining_premise:
    # check if the number of remaining quarters in the hypothesis contradicts the number of remaining quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
