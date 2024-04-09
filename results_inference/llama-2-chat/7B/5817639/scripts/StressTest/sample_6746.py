flora_leaves_premise = "2 hours after Ed"
flora_leaves_hypothesis = "more than 2 hours after Ed"

# the hypothesis talks about the time difference between Flora and Ed, referenced also in the premise
if flora_leaves_hypothesis > flora_leaves_premise:
    # check if the hypothesis value contradicts the estimate of "2 hours after Ed"
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference, any time greater than "2 hours after Ed" is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
