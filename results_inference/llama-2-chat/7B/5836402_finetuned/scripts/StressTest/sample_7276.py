mph_premise = 400
mph_hypothesis = 100

# the hypothesis talks about the driving rate of Molly and Max, referenced also in the premise
if mph_hypothesis >= mph_premise:
    # check if the hypothesis value contradicts the estimate of less than'mph_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving rate
    # any driving rate less than'mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
