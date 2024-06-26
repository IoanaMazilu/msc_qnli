ration_premise = 2/4/6
ration_hypothesis = 2600

# the hypothesis refers to the number of people in the ration mentioned in the premise
if ration_hypothesis <= ration_premise:
    # check if the estimate of 'ration_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
