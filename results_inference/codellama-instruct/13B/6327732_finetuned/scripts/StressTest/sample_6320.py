apples_maddie_premise = 4
apples_mike_premise = 2
apples_maddie_hypothesis = 6
apples_mike_hypothesis = 2

# the hypothesis refers to the number of apples Maddie has after giving 2 to Mike
if apples_maddie_hypothesis!= apples_maddie_premise - apples_mike_premise:
    # check if the hypothesis value contradicts the number of apples Maddie has after giving 2 to Mike
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has after giving 2 to Mike
    # any number of apples greater than 'apples_maddie_premise - apples_mike_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
