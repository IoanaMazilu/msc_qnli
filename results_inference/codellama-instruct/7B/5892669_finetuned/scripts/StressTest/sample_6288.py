kiwi_fruit_weight_premise = 8
kiwi_fruit_weight_hypothesis = 5
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis refers to the weight and rate of kiwi fruit mentioned in the premise
if kiwi_fruit_weight_premise <= kiwi_fruit_weight_hypothesis:
    # check if the estimate of 'kiwi_fruit_weight_hypothesis' contradicts the weight of kiwi fruit in the premise
    label = "contradiction"
elif average_rate_hypothesis!= average_rate_premise:
    # check if the rate of kiwi fruit in the hypothesis contradicts the rate of kiwi fruit reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
