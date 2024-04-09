bird1_speed_premise = 7
bird1_speed_hypothesis = 4
bird2_speed_premise = 1
bird2_speed_hypothesis = 1

# the hypothesis refers to the speed of the two birds mentioned in the premise
if bird1_speed_hypothesis >= bird1_speed_premise:
    # check if the speed of the first bird in the hypothesis contradicts the estimate of less than 'bird1_speed_premise'
    label = "contradiction"
elif bird2_speed_hypothesis!= bird2_speed_premise:
    # check if the speed of the second bird in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the first bird
    # any speed less than 'bird1_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
