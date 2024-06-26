apple_maddie_premise = 18
apple_mike_premise = 22
apple_maddie_hypothesis = 48

# the hypothesis talks about the number of apples Maddie has, referenced also in the premise
if apple_maddie_hypothesis <= apple_maddie_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apple_maddie_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples greater than 'apple_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)