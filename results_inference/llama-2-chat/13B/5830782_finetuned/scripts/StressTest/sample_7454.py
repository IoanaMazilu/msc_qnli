T_premise = 105
T_hypothesis = 105

# the hypothesis refers to the same value of T mentioned in the premise
if T_hypothesis >= T_premise:
    # check if the hypothesis contradicts the premise by stating T is greater than or equal to T
    label = "contradiction"
elif T_hypothesis < T_premise:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
