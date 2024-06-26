west_bird_speed_premise = 7
west_bird_speed_hypothesis = 4
east_bird_speed_premise = 1
east_bird_speed_hypothesis = 1

# the hypothesis talks about the speed of the two birds, referenced also in the premise
if west_bird_speed_hypothesis >= west_bird_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'west_bird_speed_premise'
    label = "contradiction"
elif east_bird_speed_hypothesis!= east_bird_speed_premise:
    # check if the speed of the second bird in the hypothesis contradicts the speed of the second bird reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the first bird
    # any speed of the first bird less than 'west_bird_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
