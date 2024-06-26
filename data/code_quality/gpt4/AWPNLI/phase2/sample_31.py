quarters_initial_premise = 760.0
quarters_spent_premise = 418.0
quarters_current_hypothesis = 341.0

# the hypothesis refers to the current number of quarters, which can be calculated from the premise
# compute the current number of quarters in the premise
quarters_current_premise = quarters_initial_premise - quarters_spent_premise
if quarters_current_hypothesis != quarters_current_premise:
    # check if the current number of quarters in the hypothesis contradicts the current number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
