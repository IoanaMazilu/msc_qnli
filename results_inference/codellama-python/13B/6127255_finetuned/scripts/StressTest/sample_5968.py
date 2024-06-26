first_leg_premise = 28
first_leg_hypothesis = 38

# the hypothesis talks about the time Dawson runs the first leg of the course, referenced also in the premise
if first_leg_hypothesis <= first_leg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'first_leg_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Dawson runs the first leg
    # any time greater than 'first_leg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
