first_leg_time_premise = 28
first_leg_time_hypothesis = 38

# the hypothesis talks about the time Dawson took to run the first leg of the course, referenced also in the premise
if first_leg_time_hypothesis <= first_leg_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'first_leg_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Dawson took to run the first leg
    # any time greater than 'first_leg_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
