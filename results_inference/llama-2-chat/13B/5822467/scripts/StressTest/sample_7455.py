maddie_apples_premise = 48
maddie_apples_hypothesis = 18

# the hypothesis refers to the number of apples Maddie has after giving 22 to Mike
if maddie_apples_hypothesis <= maddie_apples_premise - 22:
    # check if the hypothesis value contradicts the estimate of'maddie_apples_premise' minus the number of apples given to Mike
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has left
    # any number of apples greater than'maddie_apples_premise' - '22' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
