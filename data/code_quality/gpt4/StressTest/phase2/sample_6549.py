bird_one_speed_premise = 4
bird_one_speed_hypothesis = 7
bird_two_speed_premise = 1
bird_two_speed_hypothesis = 1

# the hypothesis refers to the speeds of two birds mentioned in the premise
if bird_one_speed_hypothesis < bird_one_speed_premise:
    # check if the estimate of 'bird_one_speed_hypothesis' contradicts the speed of bird one in the premise
    label = "contradiction"
elif bird_two_speed_hypothesis != bird_two_speed_premise:
    # check if the speed of bird two in the hypothesis contradicts the speed of bird two reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
