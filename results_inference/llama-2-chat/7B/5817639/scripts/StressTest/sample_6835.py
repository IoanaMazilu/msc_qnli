apple_premise = 4
apple_hypothesis = 5

# check if the hypothesis value contradicts the estimate of more than 'apple_premise'
if apple_hypothesis <= apple_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples greater than 'apple_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
