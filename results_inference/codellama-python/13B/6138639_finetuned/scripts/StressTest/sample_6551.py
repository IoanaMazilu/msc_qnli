speed_bird1_premise = 4
speed_bird1_hypothesis = 3
speed_bird2_premise = 1
speed_bird2_hypothesis = 1

# the hypothesis talks about the speed of the two birds, referenced also in the premise
if speed_bird1_hypothesis!= speed_bird1_premise:
    # check if the speed of bird 1 in the hypothesis contradicts the speed of bird 1 reported in the premise
    label = "contradiction"
elif speed_bird2_hypothesis!= speed_bird2_premise:
    # check if the speed of bird 2 in the hypothesis contradicts the speed of bird 2 reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
