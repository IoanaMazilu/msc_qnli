speed_first_bird_premise = 7
speed_first_bird_hypothesis = 4
speed_second_bird_premise = 1
speed_second_bird_hypothesis = 1

# the hypothesis refers to the speed of the first and second birds mentioned in the premise
if speed_first_bird_hypothesis >= speed_first_bird_premise:
    # check if the speed of the first bird in the hypothesis contradicts the premise
    label = "contradiction"
elif speed_second_bird_hypothesis!= speed_second_bird_premise:
    # check if the speed of the second bird in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the first bird
    # any speed less than'speed_first_bird_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
