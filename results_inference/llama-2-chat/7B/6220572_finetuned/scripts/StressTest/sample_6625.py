sheep_to_horses_premise = 1/7
sheep_to_horses_hypothesis = 6/7

# the hypothesis refers to the ratio between sheep and horses at the Stewart farm, also referenced in the premise
if sheep_to_horses_hypothesis == sheep_to_horses_premise:
    # check if the ratio in the hypothesis matches the ratio in the premise
    label = "entailment"
elif sheep_to_horses_hypothesis <= sheep_to_horses_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than'sheep_to_horses_premise' in the premise
    label = "contradiction"
else:
    # any ratio greater than'sheep_to_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
