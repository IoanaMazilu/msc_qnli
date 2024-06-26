cooking_speed_increase_premise = 0.4
cooking_speed_increase_hypothesis = 0.4

# the hypothesis mentions the cooking speed increase of the new saucepans, which is also mentioned in the premise
if cooking_speed_increase_hypothesis!= cooking_speed_increase_premise:
    # check if the cooking speed increase in the hypothesis contradicts the cooking speed increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
