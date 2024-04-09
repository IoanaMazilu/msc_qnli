T_premise = 105
T_hypothesis = 105
K_premise = (T_premise * 9 / 5) + 32
K_hypothesis = (T_hypothesis * 9 / 4) + 32

# the hypothesis refers to the same situation as the premise, but with a different condition for T
if T_premise <= T_hypothesis:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific value for T
    # any value of T greater than 'T_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
