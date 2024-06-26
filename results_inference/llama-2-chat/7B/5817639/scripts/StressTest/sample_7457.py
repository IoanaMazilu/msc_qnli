apples_premise = 48
apples_hypothesis = 88

# the hypothesis talks about the number of apples Maddie has after giving some to Mike
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the estimate of 'apples_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of apples Maddie has before giving any to Mike
    # any number of apples greater than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
