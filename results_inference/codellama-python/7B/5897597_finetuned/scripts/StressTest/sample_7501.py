pat_speed_premise = 1
pat_speed_hypothesis = 9
cara_speed_premise = 5
cara_speed_hypothesis = 5

# the hypothesis talks about the running speeds of Pat and Cara, referenced also in the premise
if pat_speed_hypothesis <= pat_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pat_speed_premise'
    label = "contradiction"
elif cara_speed_hypothesis!= cara_speed_premise:
    # check if the running speed of Cara in the hypothesis contradicts the running speed of Cara reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the running speed of Pat
    # any speed of Pat greater than 'pat_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
