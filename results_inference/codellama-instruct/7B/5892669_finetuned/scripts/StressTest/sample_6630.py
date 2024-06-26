distance_covered_premise = 500
distance_covered_hypothesis = 800
speed_premise = 15
speed_hypothesis = 15

# the hypothesis refers to the distance covered and speed mentioned in the premise
if distance_covered_premise >= distance_covered_hypothesis:
    # check if the estimate of 'distance_covered_hypothesis' contradicts the distance covered in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
