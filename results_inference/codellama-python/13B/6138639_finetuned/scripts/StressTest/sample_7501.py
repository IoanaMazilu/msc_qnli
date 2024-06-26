pat_speed_premise = 1
cara_speed_premise = 5
pat_speed_hypothesis = 9
cara_speed_hypothesis = 5

# the hypothesis talks about the speed of Pat and Cara, referenced also in the premise
if pat_speed_hypothesis <= pat_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pat_speed_premise'
    label = "contradiction"
elif cara_speed_hypothesis!= cara_speed_premise:
    # check if the speed of Cara in the hypothesis contradicts the speed of Cara reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Pat
    # any speed of Pat greater than 'pat_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
