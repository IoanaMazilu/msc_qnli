distance_covered_premise = 500
distance_covered_hypothesis = 800
speed_sandy = 15

# the hypothesis refers to the distance covered by Sandy, also mentioned in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the distance in the hypothesis contradicts the distance covered in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance covered in the premise, we can infer entailment
    label = "entailment"

print(label)
