yankees_mets_ratio_premise = 2/1
yankees_mets_ratio_hypothesis = 7/1
mets_redsox_ratio_premise = 3/7
mets_redsox_ratio_hypothesis = 3/7

# the hypothesis refers to the ratios of different fans mentioned in the premise
if yankees_mets_ratio_hypothesis < yankees_mets_ratio_premise:
    # check if the yankees to mets ratio in the hypothesis contradicts the same ratio in the premise
    label = "contradiction"
elif mets_redsox_ratio_hypothesis != mets_redsox_ratio_premise:
    # check if the mets to red sox ratio in the hypothesis contradicts the same ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
