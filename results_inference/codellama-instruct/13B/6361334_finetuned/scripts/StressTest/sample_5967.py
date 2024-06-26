dawson_first_leg_premise = 38
dawson_first_leg_hypothesis = 28

# the hypothesis refers to the time taken by Dawson to run the first leg of the course
if dawson_first_leg_hypothesis <= dawson_first_leg_premise:
    # check if the estimate of 'dawson_first_leg_hypothesis' contradicts the time taken by Dawson in the premise
    label = "contradiction"
else:
    # the premise gives an exact time taken by Dawson to run the first leg of the course
    # any time greater than 'dawson_first_leg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
