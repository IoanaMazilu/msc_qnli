distance_premise = 500
distance_hypothesis = 800
speed_premise = 15
speed_hypothesis = 15

# the hypothesis refers to the distance covered and speed of Sandy mentioned in the premise
if distance_premise >= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif speed_premise!= speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
