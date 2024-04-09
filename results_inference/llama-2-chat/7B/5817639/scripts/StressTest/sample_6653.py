apples_premise = 18
apples_hypothesis = 58

# the hypothesis talks about the number of apples Maddie has after giving 12 to Mike
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the estimate of 'apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples greater than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
