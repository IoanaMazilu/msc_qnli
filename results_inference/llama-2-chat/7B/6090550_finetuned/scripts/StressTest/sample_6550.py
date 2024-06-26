bird1_speed_premise = 7
bird1_speed_hypothesis = 4
bird2_speed_premise = 1
bird2_speed_hypothesis = 1

# the hypothesis talks about the speed of two birds flying towards each other, referenced also in the premise
if bird1_speed_hypothesis < bird1_speed_premise:
    # check if the speed of the first bird in the hypothesis contradicts the premise
    label = "contradiction"
elif bird2_speed_hypothesis!= bird2_speed_premise:
    # check if the speed of the second bird in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
