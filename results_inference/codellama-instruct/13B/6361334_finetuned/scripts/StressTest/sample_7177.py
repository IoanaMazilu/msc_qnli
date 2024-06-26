ration_premise = 3800
ration_hypothesis = 4800

# the hypothesis refers to the total number of people in the ration, mentioned in the premise
if ration_hypothesis <= ration_premise:
    # check if the estimate of 'ration_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
