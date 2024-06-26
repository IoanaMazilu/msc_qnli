distance_premise = 31
distance_hypothesis = 81

# the hypothesis refers to the distance Yolanda walked, mentioned in the premise
if distance_premise >= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance Yolanda walked in the premise
    label = "contradiction"
elif distance_hypothesis <= distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
