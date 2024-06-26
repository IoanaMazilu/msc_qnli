kiwi_weight_premise = 8
kiwi_weight_hypothesis = 8
rate_premise = 360
rate_hypothesis = 360

# the hypothesis refers to the weight and rate of kiwi fruit mentioned in the premise
if kiwi_weight_hypothesis <= kiwi_weight_premise:
    # check if the hypothesis value contradicts the estimate of 'kiwi_weight_premise'
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
