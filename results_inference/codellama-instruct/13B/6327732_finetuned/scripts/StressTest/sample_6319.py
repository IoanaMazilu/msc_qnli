apples_maddie_premise = 7
apples_maddie_hypothesis = 4

# the hypothesis refers to the number of apples Maddie has after giving 2 to Mike
# the premise mentions that Maddie has less than 7 apples
if apples_maddie_hypothesis <= apples_maddie_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apples_maddie_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples greater than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
