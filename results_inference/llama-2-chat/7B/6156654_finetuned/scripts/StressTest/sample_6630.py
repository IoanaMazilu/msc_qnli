distance_premise = 500
distance_hypothesis = 800
speed = 15

# the hypothesis refers to the distance Sandy covers, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif speed!= 15:
    # check if the speed of Sandy in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
