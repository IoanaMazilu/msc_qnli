# Premise: Smitha bought more than 5 Kg of kiwi fruit at an average rate of 360.
# Hypothesis: Smitha bought 8 Kg of kiwi fruit at an average rate of 360.
# Golden Label: neutral

kiwi_weight_premise = 5
kiwi_weight_hypothesis = 8
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis talks about the weight of kiwi fruit and the average rate, both referenced also in the premise
if kiwi_weight_hypothesis <= kiwi_weight_premise:
    # check if the hypothesis value contradicts the estimate of more than 'kiwi_weight_premise' kg
    label = "contradiction"
elif average_rate_hypothesis != average_rate_premise:
    # check if the average rate in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of kiwi fruit
    # any weight greater than 'kiwi_weight_premise' kg is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

