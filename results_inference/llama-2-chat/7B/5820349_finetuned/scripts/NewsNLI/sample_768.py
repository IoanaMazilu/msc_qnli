cooking_time_faster_premise = 0.40
cooking_time_faster_hypothesis = 0.40

# the hypothesis mentions the cooking time advantage of the new saucepans, which is also mentioned in the premise
if cooking_time_faster_hypothesis!= cooking_time_faster_premise:
    # check if the cooking time advantage in the hypothesis contradicts the cooking time advantage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
