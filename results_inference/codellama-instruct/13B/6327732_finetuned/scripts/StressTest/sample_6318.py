apples_maddie_premise = 4
apples_mike_hypothesis = 2

# the hypothesis refers to the number of apples Maddie has left after giving 2 to Mike
if apples_maddie_premise - apples_mike_hypothesis < 7:
    # check if the estimate of 'apples_maddie_premise' contradicts the number of apples Maddie has left after giving 2 to Mike
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has left after giving 2 to Mike
    # any number of apples less than 7 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
