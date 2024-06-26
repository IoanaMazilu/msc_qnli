cooking_speed_premise = 0.4
cooking_speed_hypothesis = 0.4

# the hypothesis mentions the cooking speed of the saucepans, which is also mentioned in the premise
if cooking_speed_hypothesis!= cooking_speed_premise:
    # check if the cooking speed in the hypothesis contradicts the cooking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
