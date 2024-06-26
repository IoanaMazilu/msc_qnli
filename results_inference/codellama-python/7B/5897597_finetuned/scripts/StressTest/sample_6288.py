kiwi_weight_premise = 8
kiwi_weight_hypothesis = 5
kiwi_rate_premise = 360
kiwi_rate_hypothesis = 360

# the hypothesis refers to the weight and rate of kiwi fruit bought by Smitha, mentioned in the premise
if kiwi_weight_premise <= kiwi_weight_hypothesis:
    # check if the weight of kiwi fruit in the hypothesis contradicts the weight of kiwi fruit in the premise
    label = "contradiction"
elif kiwi_rate_hypothesis!= kiwi_rate_premise:
    # check if the rate of kiwi fruit in the hypothesis contradicts the rate of kiwi fruit in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
