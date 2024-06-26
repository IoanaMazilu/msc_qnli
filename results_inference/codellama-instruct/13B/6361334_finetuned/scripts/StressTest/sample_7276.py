mph_premise = 400
mph_hypothesis = 100

# the hypothesis refers to the rate of driving mentioned in the premise
if mph_hypothesis >= mph_premise:
    # check if the estimate of'mph_hypothesis' contradicts the rate of driving in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate of driving
    # any rate of driving less than'mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
