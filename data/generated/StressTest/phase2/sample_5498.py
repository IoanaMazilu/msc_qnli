# Premise: In a certain town, the ratio of NY Yankees fans to NY Mets fans is 2:1, and the ratio of NY Mets fans to Boston Red Sox fans is 3:7.
# Hypothesis: In a certain town, the ratio of NY Yankees fans to NY Mets fans is 8:1, and the ratio of NY Mets fans to Boston Red Sox fans is 3:7.
# Golden Label: contradiction

yankees_to_mets_premise = 2 / 1
yankees_to_mets_hypothesis = 8 / 1
mets_to_redsox_premise = 3 / 7
mets_to_redsox_hypothesis = 3 / 7

# the hypothesis refers to the same ratios of fans as the premise
if yankees_to_mets_hypothesis != yankees_to_mets_premise:
    # check if the ratio of Yankees to Mets fans in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif mets_to_redsox_hypothesis != mets_to_redsox_premise:
    # check if the ratio of Mets to Red Sox fans in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

