apple_maddie_premise = 4
apple_mike_premise = 2
apple_maddie_hypothesis = 7

# the hypothesis talks about the number of apples Maddie has left after giving 2 to Mike
if apple_maddie_hypothesis <= apple_maddie_premise - apple_mike_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apple_maddie_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has left
    # any number of apples greater than 'apple_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
