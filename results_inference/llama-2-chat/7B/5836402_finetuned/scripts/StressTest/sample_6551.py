bird1_speed_premise = 4
bird1_speed_hypothesis = 3
bird2_speed_premise = 1
bird2_speed_hypothesis = 1

# the hypothesis refers to the speed of the two birds mentioned in the premise
if bird1_speed_hypothesis!= bird1_speed_premise:
    # check if the speed of the first bird in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif bird2_speed_hypothesis!= bird2_speed_premise:
    # check if the speed of the second bird in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
