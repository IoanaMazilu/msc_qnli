joined_premise = 8
joined_hypothesis = 2

# the hypothesis talks about the time Jose joined, referenced also in the premise
if joined_hypothesis <= joined_premise:
    # check if the hypothesis value contradicts the estimate of less than 'joined_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Jose joined
    # any time greater than 'joined_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
