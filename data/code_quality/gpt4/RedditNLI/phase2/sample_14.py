increase_needed_premise = 1.5
increase_needed_hypothesis = 1.5

# the hypothesis and premise mention the amount of barrels that need to be found to avoid a shortfall
if increase_needed_hypothesis != increase_needed_premise:
    # check if the amount needed in the hypothesis contradicts the amount needed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
