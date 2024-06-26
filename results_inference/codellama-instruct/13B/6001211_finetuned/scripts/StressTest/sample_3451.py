months_joined_premise = 8
months_joined_hypothesis = 2

# the hypothesis talks about the time when Jose joined, referenced also in the premise
if months_joined_hypothesis >= months_joined_premise:
    # check if the hypothesis value contradicts the estimate of less than'months_joined_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when Jose joined
    # any time less than'months_joined_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
