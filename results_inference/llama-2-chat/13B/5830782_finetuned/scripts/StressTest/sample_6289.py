kiwi_weight_premise = 5
kiwi_weight_hypothesis = 8
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis refers to the weight of the kiwi fruit and the average rate mentioned in the premise
if kiwi_weight_hypothesis <= kiwi_weight_premise:
    # check if the weight of 'kiwi_weight_hypothesis' contradicts the weight of kiwi fruit in the premise
    label = "contradiction"
elif average_rate_hypothesis!= average_rate_premise:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of the kiwi fruit
    # any weight greater than 'kiwi_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
