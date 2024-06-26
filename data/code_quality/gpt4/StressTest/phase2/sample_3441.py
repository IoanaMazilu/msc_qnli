distance_covered_premise = 600
distance_covered_hypothesis = 100
speed_sandy = 18

# the hypothesis refers to the distance covered by Sandy, also mentioned in the premise
if distance_covered_hypothesis >= distance_covered_premise:
    # check if the distance in the hypothesis contradicts the distance covered by Sandy in the premise
    label = "contradiction"
elif speed_sandy != 18:
    # check if the speed of Sandy in the hypothesis contradicts the speed of Sandy in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
