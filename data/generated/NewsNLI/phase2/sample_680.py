# Premise: '' The Storm Prediction Center estimates the total will be around 75 when all surveys are complete,'' the weather service website said.
# Hypothesis: Confirmed tornadoes are expected to be around 75.
# Golden Label: neutral

estimated_tornadoes_premise = 75
confirmed_tornadoes_hypothesis = 75

# the hypothesis mentions the number of confirmed tornadoes, which is the same as the estimated number in the premise
if confirmed_tornadoes_hypothesis != estimated_tornadoes_premise:
    # check if the number of confirmed tornadoes in the hypothesis contradicts the estimated number in the premise
    label = "contradiction"
else:
    # if the number of confirmed tornadoes in the hypothesis does not contradict the estimated number in the premise, we can infer entailment
    label = "entailment"

print(label)

