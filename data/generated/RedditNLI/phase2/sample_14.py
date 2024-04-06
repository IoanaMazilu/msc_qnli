# Premise: World oil demand will exceed supply in the second half of the year unless we can increase production by 1.5 million barrels a day.
# Hypothesis: Oil markets facing shortfall in the second half (ie. demand will surpass supply unless we fond another 1.5 million barrels of oil a day).
# Golden Label: entailment

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

