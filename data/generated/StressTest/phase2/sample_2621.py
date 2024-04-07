# Premise: In a certain town, the ratio of NY Yankees fans to NY Mets fans is 3:2, and the ratio of NY Mets fans to Boston Red Sox fans is 4:5.
# Hypothesis: In a certain town, the ratio of NY Yankees fans to NY Mets fans is 5:2, and the ratio of NY Mets fans to Boston Red Sox fans is 4:5.
# Golden Label: contradiction

yankees_mets_ratio_premise = 3 / 2
yankees_mets_ratio_hypothesis = 5 / 2
mets_redsox_ratio_premise = 4 / 5
mets_redsox_ratio_hypothesis = 4 / 5

# the hypothesis refers to the ratios of fans mentioned in the premise
if yankees_mets_ratio_premise != yankees_mets_ratio_hypothesis:
    # check if the Yankees to Mets fans ratio in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif mets_redsox_ratio_premise != mets_redsox_ratio_hypothesis:
    # check if the Mets to Red Sox fans ratio in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

