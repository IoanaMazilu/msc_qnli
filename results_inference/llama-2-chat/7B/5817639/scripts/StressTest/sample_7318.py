minutes_premise = 78
minutes_hypothesis = 18

# the hypothesis talks about the time it takes Jim to catch up to Cara, referenced also in the premise
if minutes_hypothesis <= minutes_premise:
    # check if the hypothesis value contradicts the estimate of more than'minutes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes Jim to catch up to Cara
    # any time greater than'minutes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
