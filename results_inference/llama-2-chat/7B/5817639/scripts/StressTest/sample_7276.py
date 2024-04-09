rate_premise = 400
rate_hypothesis = 100

# the hypothesis talks about the speed of Molly and Max, referenced also in the premise
if rate_hypothesis <= rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than 'rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
