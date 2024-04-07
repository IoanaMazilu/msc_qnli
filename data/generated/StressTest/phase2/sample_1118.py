# Premise: Raj and Roshan has some money with them in the ratio 5:4 respectively.
# Hypothesis: Raj and Roshan has some money with them in the ratio more than 5:4 respectively.
# Golden Label: contradiction

raj_roshan_ratio_premise = 5/4
raj_roshan_ratio_hypothesis = 5/4

# the hypothesis refers to the ratio of money Raj and Roshan have, mentioned in the premise
if raj_roshan_ratio_premise >= raj_roshan_ratio_hypothesis:
    # check if the hypothesis ratio contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio for the money Raj and Roshan have
    # any ratio greater than 'raj_roshan_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

