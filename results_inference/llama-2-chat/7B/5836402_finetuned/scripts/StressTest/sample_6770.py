total_ration_premise = 6600
total_ration_hypothesis = 6600

# the hypothesis refers to the total number in the ratio mentioned in the premise
if total_ration_hypothesis >= total_ration_premise:
    # check if the estimate of 'total_ration_hypothesis' contradicts the total number in the ratio from the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
