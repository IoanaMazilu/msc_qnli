maddie_apples_premise = 18
maddie_apples_hypothesis = 58

# the hypothesis refers to the number of apples Maddie has after giving 12 to Mike
if maddie_apples_hypothesis - 12 <= maddie_apples_premise:
    # check if the estimate of'maddie_apples_hypothesis' contradicts the number of apples Maddie has after giving 12 to Mike
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has after giving 12 to Mike
    # any number of apples greater than'maddie_apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
