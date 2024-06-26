cooking_speed_premise = 0.40
cooking_speed_hypothesis = 0.40

# the hypothesis mentions the cooking speed improvement of the saucepans, which is also mentioned in the premise
if cooking_speed_hypothesis!= cooking_speed_premise:
    # check if the cooking speed improvement in the hypothesis contradicts the cooking speed improvement reported in the premise
    label = "contradiction"
else:
    # if the cooking speed improvement in the hypothesis does not contradict the cooking speed improvement in the premise, we can infer entailment
    label = "entailment"

print(label)
