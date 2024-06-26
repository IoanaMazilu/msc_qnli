sum_premise = 288
sum_hypothesis = 888

# the hypothesis refers to the same sum mentioned in the premise
if sum_premise!= sum_hypothesis:
    # check if the sum in the hypothesis contradicts the sum mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
