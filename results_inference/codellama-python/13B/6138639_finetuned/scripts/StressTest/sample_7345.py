slump_premise = 68
slump_hypothesis = 28

# the hypothesis talks about the slump of crude oil prices, referenced also in the premise
if slump_hypothesis >= slump_premise:
    # check if the hypothesis value contradicts the estimate of less than'slump_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the slump of crude oil prices
    # any slump less than'slump_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
