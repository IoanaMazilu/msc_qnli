distance_covered_premise = 40.0
distance_covered_hypothesis = 5.0
speed_premise = 8.0
speed_hypothesis = 8.0

# the hypothesis mentions the distance covered and speed, which are also mentioned in the premise
if distance_covered_hypothesis!= distance_covered_premise:
    # check if the distance covered in the hypothesis contradicts the distance covered in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
