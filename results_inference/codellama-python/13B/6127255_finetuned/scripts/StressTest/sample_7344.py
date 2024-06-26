slump_percentage_premise = 28
slump_percentage_hypothesis = 68
increase_percentage_premise = 5
increase_percentage_hypothesis = 5

# the hypothesis refers to the slump and increase percentage of crude oil price mentioned in the premise
if slump_percentage_hypothesis < slump_percentage_premise:
    # check if the estimate of'slump_percentage_hypothesis' contradicts the slump percentage in the premise
    label = "contradiction"
elif increase_percentage_hypothesis!= increase_percentage_premise:
    # check if the increase percentage in the hypothesis contradicts the increase percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
