kiwi_weight_premise = 5
kiwi_weight_hypothesis = 8
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis talks about the weight and average rate of kiwi fruit bought by Smitha, referenced also in the premise
if kiwi_weight_hypothesis <= kiwi_weight_premise:
    # check if the hypothesis value contradicts the estimate of more than 'kiwi_weight_premise'
    label = "contradiction"
elif average_rate_hypothesis!= average_rate_premise:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of kiwi fruit
    # any weight greater than 'kiwi_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
