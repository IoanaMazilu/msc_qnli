minutes_premise = 10
minutes_hypothesis = 60

# the hypothesis talks about the time when Pat stops to stretch, referenced also in the premise
if minutes_hypothesis <= minutes_premise:
    # check if the hypothesis value contradicts the number of minutes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when Pat stops
    # any time greater than'minutes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
