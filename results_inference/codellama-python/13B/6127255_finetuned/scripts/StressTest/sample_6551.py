bird1_speed_premise = 4
bird1_speed_hypothesis = 3
bird2_speed_premise = 1
bird2_speed_hypothesis = 1

# the hypothesis refers to the speed of the birds mentioned in the premise
if bird1_speed_premise!= bird1_speed_hypothesis:
    # check if the speed of bird1 in the hypothesis contradicts the speed of bird1 in the premise
    label = "contradiction"
elif bird2_speed_premise!= bird2_speed_hypothesis:
    # check if the speed of bird2 in the hypothesis contradicts the speed of bird2 in the premise
    label = "contradiction"
else:
    # if the speeds of the birds in the hypothesis do not contradict the speeds of the birds in the premise, we can infer entailment
    label = "entailment"

print(label)
