premise_time = 6
hypothesis_time = 7

# the hypothesis refers to the time taken by Henry to run the second leg of the course
if hypothesis_time <= premise_time:
    # check if the hypothesis value contradicts the estimate of more than 'premise_time'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Henry to run the second leg of the course
    # any time taken by Henry to run the second leg of the course greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
