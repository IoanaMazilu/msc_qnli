distance_covered_premise = 100
distance_covered_hypothesis = 600
speed_premise = 18
speed_hypothesis = 18

# the hypothesis refers to the same scenario as the premise, but with different distances covered
if distance_covered_hypothesis <= distance_covered_premise and speed_hypothesis == speed_premise:
    # check if the distance covered in the hypothesis contradicts the premise's estimate
    label = "contradiction"
elif distance_covered_hypothesis > distance_covered_premise and speed_hypothesis == speed_premise:
    # the premise gives an estimate for the distance covered
    # any distance greater than 'distance_covered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
