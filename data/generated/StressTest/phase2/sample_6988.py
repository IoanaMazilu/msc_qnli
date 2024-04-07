# Premise: The ratio of the ages of Anil and his son at present is more than 2:3.
# Hypothesis: The ratio of the ages of Anil and his son at present is 7:3.
# Golden Label: neutral

anil_son_ratio_premise = 2/3
anil_son_ratio_hypothesis = 7/3

# the hypothesis gives a specific ratio for Anil and his son's ages, referenced also in the premise
if anil_son_ratio_hypothesis <= anil_son_ratio_premise:
    # check if the hypothesis ratio contradicts the estimate of more than 'anil_son_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of Anil and his son's ages
    # any ratio greater than 'anil_son_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

