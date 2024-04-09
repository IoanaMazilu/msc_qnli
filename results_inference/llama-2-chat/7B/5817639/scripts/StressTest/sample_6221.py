amount_premise = 100
amount_hypothesis = 50

# the hypothesis refers to a different ratio than the premise
if amount_hypothesis <= amount_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio, while the hypothesis gives a different one
    # any ratio less than the one in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
