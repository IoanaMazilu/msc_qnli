bird1_speed_premise = 7
bird2_speed_premise = 1
bird1_speed_hypothesis = 4
bird2_speed_hypothesis = 1

# the hypothesis refers to the speed of the two birds mentioned in the premise
if bird1_speed_premise >= bird1_speed_hypothesis:
    # check if the estimate of 'bird1_speed_hypothesis' contradicts the speed of the first bird in the premise
    label = "contradiction"
elif bird2_speed_hypothesis!= bird2_speed_premise:
    # check if the speed of the second bird in the hypothesis contradicts the speed of the second bird reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
