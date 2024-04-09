speed_bird1_premise = 4
speed_bird1_hypothesis = 3
speed_bird2_premise = 1
speed_bird2_hypothesis = 1

# the hypothesis refers to the speed of the two birds mentioned in the premise
if speed_bird1_premise!= speed_bird1_hypothesis:
    # check if the speed of bird1 in the hypothesis contradicts the speed of bird1 reported in the premise
    label = "contradiction"
elif speed_bird2_premise!= speed_bird2_hypothesis:
    # check if the speed of bird2 in the hypothesis contradicts the speed of bird2 reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
