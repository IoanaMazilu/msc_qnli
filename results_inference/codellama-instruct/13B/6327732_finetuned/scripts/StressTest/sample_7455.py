apples_maddie_premise = 48
apples_mike_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has after giving some to Mike
if apples_maddie_premise - apples_mike_hypothesis > 18:
    # check if the estimate of 'apples_maddie_premise' contradicts the number of apples Maddie has after giving some to Mike
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has after giving some to Mike
    # any number of apples greater than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
