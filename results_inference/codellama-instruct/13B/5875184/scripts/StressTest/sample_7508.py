premise_time = 20
hypothesis_time = 80

# the hypothesis refers to the time it takes for Pat to stretch and Cara to run
if hypothesis_time <= premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes for Pat to stretch and Cara to run
    # any time greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
