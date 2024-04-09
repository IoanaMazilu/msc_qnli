apples_billy_premise = 4
apples_billy_hypothesis = 5

# the hypothesis talks about the number of apples Billy has, which is also referenced in the premise
if apples_billy_hypothesis <= apples_billy_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_billy_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples greater than 'apples_billy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
