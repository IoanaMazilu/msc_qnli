T_premise = 105
T_hypothesis = 5/9 * (K_hypothesis - 32)

# the hypothesis refers to the temperature T and the value of K
if T_hypothesis <= T_premise:
    # check if the estimate of 'T_hypothesis' contradicts the value of T in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the temperature T
    # any value of K greater than 'K_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
