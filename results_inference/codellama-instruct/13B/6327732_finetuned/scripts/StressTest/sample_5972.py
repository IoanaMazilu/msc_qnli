premise_time = 7
hypothesis_time = 6

# the hypothesis refers to the time taken by Henry to run the second leg of the course
if hypothesis_time < premise_time:
    # check if the hypothesis value contradicts the time taken by Henry in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the time taken by Henry to run the second leg of the course
    # any time taken by Henry greater than or equal to 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
