# Premise: Patrick has a locker with a 3 number combination.
# Hypothesis: Patrick has a locker with a more than 3 number combination.
# Golden Label: contradiction

locker_combination_premise = 3
locker_combination_hypothesis = 3

# the hypothesis refers to the number of the locker combination that is also mentioned in the premise
if locker_combination_hypothesis != locker_combination_premise:
    # check if the number of combination in the hypothesis contradicts the number of combination reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates are the same with the premise ones, we can infer entailment
    label = "entailment"

print(label)

