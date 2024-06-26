T_premise = 5/9 * (K_premise - 32)
T_hypothesis = 105

# the hypothesis refers to the temperature T and the value of K mentioned in the premise
if T_hypothesis <= T_premise:
    # check if the estimate of 'T_hypothesis' contradicts the value of T in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of T
    # any value of T greater than 'T_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
