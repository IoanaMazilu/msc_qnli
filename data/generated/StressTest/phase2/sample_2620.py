# Premise: In a certain town, the ratio of NY Yankees fans to NY Mets fans is less than 8:2, and the ratio of NY Mets fans to Boston Red Sox fans is 4:5.
# Hypothesis: In a certain town, the ratio of NY Yankees fans to NY Mets fans is 3:2, and the ratio of NY Mets fans to Boston Red Sox fans is 4:5.
# Golden Label: neutral

yankees_to_mets_premise = 8 / 2
yankees_to_mets_hypothesis = 3 / 2
mets_to_redsox_premise = 4 / 5
mets_to_redsox_hypothesis = 4 / 5

# the hypothesis refers to the ratios of different baseball fans mentioned in the premise
if yankees_to_mets_hypothesis <= yankees_to_mets_premise:
    # check if the ratio of Yankees to Mets fans in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif mets_to_redsox_hypothesis != mets_to_redsox_premise:
    # check if the ratio of Mets to Red Sox fans in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

