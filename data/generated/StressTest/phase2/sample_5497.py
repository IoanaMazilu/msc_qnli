# Premise: In a certain town, the ratio of NY Yankees fans to NY Mets fans is less than 7:1, and the ratio of NY Mets fans to Boston Red Sox fans is 3:7.
# Hypothesis: In a certain town, the ratio of NY Yankees fans to NY Mets fans is 2:1, and the ratio of NY Mets fans to Boston Red Sox fans is 3:7.
# Golden Label: neutral

yankees_mets_ratio_premise = 7
yankees_mets_ratio_hypothesis = 2
mets_redsox_ratio_premise = 3 / 7
mets_redsox_ratio_hypothesis = 3 / 7

# the hypothesis refers to the ratios of fans of different teams mentioned in the premise
if yankees_mets_ratio_hypothesis >= yankees_mets_ratio_premise:
    # check if the estimate of 'yankees_mets_ratio_hypothesis' contradicts the number of Yankees to Mets fans ratio in the premise
    label = "contradiction"
elif mets_redsox_ratio_hypothesis != mets_redsox_ratio_premise:
    # check if the ratio of Mets to Red Sox fans in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
