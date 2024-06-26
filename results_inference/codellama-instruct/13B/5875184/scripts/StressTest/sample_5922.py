premise_time = 1/2
hypothesis_time = 3/2

# the hypothesis refers to the time taken for the trip home
if hypothesis_time < premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time taken for the trip home in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken for the trip home
    # any time taken for the trip home greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
