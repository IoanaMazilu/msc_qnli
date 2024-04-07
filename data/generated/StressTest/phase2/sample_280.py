# Premise: The ratio of the ages of Mona and Sona is more than 1:5.
# Hypothesis: The ratio of the ages of Mona and Sona is 4:5.
# Golden Label: neutral

ratio_premise = 1/5
ratio_hypothesis = 4/5

# The hypothesis refers to the ratio of ages of Mona and Sona mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesized ratio contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the ratio
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

