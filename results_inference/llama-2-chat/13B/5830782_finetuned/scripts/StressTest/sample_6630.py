distance_covered_premise = 500
distance_covered_hypothesis = 800
speed_sandy = 15

# the hypothesis refers to the distance covered by Sandy, which is also mentioned in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the estimate of 'distance_covered_hypothesis' contradicts the distance covered in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
