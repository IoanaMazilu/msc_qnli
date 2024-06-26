first_leg_premise = 82
first_leg_hypothesis = 22

# the hypothesis talks about the time Paul took to run the first leg of the course, which is also referred in the premise
if first_leg_hypothesis >= first_leg_premise:
    # check if the hypothesis value contradicts the estimate of less than 'first_leg_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Paul took for the first leg
    # any time less than 'first_leg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
