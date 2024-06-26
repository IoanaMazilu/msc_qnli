minutes_premise = 10
minutes_hypothesis = 20

# the hypothesis talks about the number of minutes, referenced also in the premise
if minutes_hypothesis >= minutes_premise:
    # check if the hypothesis value contradicts the estimate of less than'minutes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of minutes
    # any number of minutes less than'minutes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
