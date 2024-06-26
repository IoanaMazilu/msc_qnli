apples_premise = 4
apples_hypothesis = 5

# the hypothesis talks about the number of apples Billy has, which is also mentioned in the premise
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples greater than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)