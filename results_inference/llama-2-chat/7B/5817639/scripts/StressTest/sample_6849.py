apple_premise = 10
apple_hypothesis = 20

# the hypothesis talks about the number of apples Billy has, referenced also in the premise
if apple_hypothesis <= apple_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apple_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples greater than 'apple_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
