T_premise = 20
T_hypothesis = 20

# the hypothesis refers to the value of T mentioned in the premise
if T_hypothesis <= T_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific value for T
    # any value of T greater than 'T_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
