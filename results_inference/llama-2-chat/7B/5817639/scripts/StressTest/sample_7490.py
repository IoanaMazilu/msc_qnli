apples_premise = 360
apples_hypothesis = 560

# the hypothesis talks about the number of apples Anita has, which is also mentioned in the premise
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the estimate of 'apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples greater than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
