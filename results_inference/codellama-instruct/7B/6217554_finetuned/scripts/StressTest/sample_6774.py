average_speed_premise = 0
average_speed_hypothesis = 0
ratio_premise = 4/2
ratio_hypothesis = 1/2

# the hypothesis gives a new ratio for the distances between A to B and B to C, which is consistent with the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
