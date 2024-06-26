anil_son_ratio_premise = 2/3
anil_son_ratio_hypothesis = 7/3

# the hypothesis refers to the ratio of ages of Anil and his son mentioned in the premise
if anil_son_ratio_hypothesis <= anil_son_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'anil_son_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio greater than 'anil_son_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
