bird1_speed_premise = 4
bird2_speed_premise = 1
bird1_speed_hypothesis = 3
bird2_speed_hypothesis = 1

# the hypothesis talks about the speed of the birds, which is also mentioned in the premise
if bird1_speed_hypothesis!= bird1_speed_premise:
    # check if the speed of the first bird in the hypothesis contradicts the speed of the first bird in the premise
    label = "contradiction"
elif bird2_speed_hypothesis!= bird2_speed_premise:
    # check if the speed of the second bird in the hypothesis contradicts the speed of the second bird in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
