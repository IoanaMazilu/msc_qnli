minutes_premise = 10
minutes_hypothesis = 20

# the hypothesis talks about the time Pat stops to stretch, referenced also in the premise
if minutes_hypothesis <= minutes_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact time when Pat stops to stretch
    # any time greater than'minutes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
