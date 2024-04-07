# Premise: Smitha bought 8 Kg of kiwi fruit at an average rate of 360.
# Hypothesis: Smitha bought more than 5 Kg of kiwi fruit at an average rate of 360.
# Golden Label: entailment

kiwi_weight_premise = 8
kiwi_weight_hypothesis = 5
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis refers to the weight of kiwi fruit bought and the average rate, mentioned also in the premise
if kiwi_weight_premise <= kiwi_weight_hypothesis:
    # check if the weight of kiwi in the hypothesis contradicts the weight of kiwi reported in the premise
    label = "contradiction"
elif average_rate_hypothesis != average_rate_premise:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

