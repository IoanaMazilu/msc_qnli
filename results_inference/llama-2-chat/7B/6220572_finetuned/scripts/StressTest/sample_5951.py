T_premise = 5/9 * (K-32)
T_hypothesis = 5/9 * (K-32)
T_value_premise = 20
T_value_hypothesis = 20

# the hypothesis refers to the condition and value of T mentioned in the premise
if T_hypothesis == T_value_premise:
    # check if the hypothesis value contradicts the value of T in the premise
    label = "contradiction"
elif T_hypothesis < T_premise:
    # check if the hypothesis estimate for T contradicts the estimate of T in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of T
    # any value of T consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
