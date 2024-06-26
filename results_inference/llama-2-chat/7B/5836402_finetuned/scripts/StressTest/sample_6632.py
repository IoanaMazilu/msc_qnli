distance_covered_premise = 500
distance_covered_hypothesis = 500
running_speed_premise = 15
running_speed_hypothesis = 15

# the hypothesis refers to the distance covered by Sandy, mentioned in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the estimate of 'distance_covered_hypothesis' contradicts the distance covered in the premise
    label = "contradiction"
elif running_speed_hypothesis!= running_speed_premise:
    # check if the running speed in the hypothesis contradicts the running speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
