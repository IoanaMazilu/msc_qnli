speed_first_bird_premise = 7
speed_first_bird_hypothesis = 4
speed_second_bird_premise = 1
speed_second_bird_hypothesis = 1

# the hypothesis talks about the speed of the two birds, referenced also in the premise
if speed_first_bird_hypothesis >= speed_first_bird_premise:
    # check if the hypothesis value contradicts the estimate of less than'speed_first_bird_premise'
    label = "contradiction"
elif speed_second_bird_hypothesis!= speed_second_bird_premise:
    # check if the speed of the second bird in the hypothesis contradicts the speed of the second bird reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the first bird
    # any speed of the first bird less than'speed_first_bird_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
