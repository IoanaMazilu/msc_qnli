drained_value_premise = 5.12
drained_value_hypothesis = 1

# the hypothesis and premise mention the drained value in US dollars from current account deficit in July 2017
if drained_value_hypothesis > drained_value_premise:
    # check if the drained value in the hypothesis contradicts the drained value in the premise
    label = "contradiction"
elif drained_value_hypothesis < drained_value_premise:
    # check if the drained value in the hypothesis is less than the drained value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
