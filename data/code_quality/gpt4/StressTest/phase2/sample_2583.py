apples_purchased_premise = 8
apples_purchased_hypothesis = 7
rate_apples_premise = 70
rate_apples_hypothesis = 70
mangoes_purchased_premise = 9
mangoes_purchased_hypothesis = 9
rate_mangoes_premise = 55
rate_mangoes_hypothesis = 55

# the hypothesis refers to the number and rate of purchased apples and mangoes mentioned in the premise
if apples_purchased_premise <= apples_purchased_hypothesis:
    # check if the estimate of 'apples_purchased_hypothesis' contradicts the number of apples purchased in the premise
    label = "contradiction"
elif rate_apples_hypothesis != rate_apples_premise:
    # check if the rate of apples in the hypothesis contradicts the rate of apples reported in the premise
    label = "contradiction"
elif mangoes_purchased_hypothesis != mangoes_purchased_premise:
    # check if the number of purchased mangoes in the hypothesis contradicts the number of purchased mangoes reported in the premise
    label = "contradiction"
elif rate_mangoes_hypothesis != rate_mangoes_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
