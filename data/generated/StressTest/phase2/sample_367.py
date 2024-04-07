# Premise: In a certain town, the ratio of NY Yankees fans to NY Mets fans is less than 4:2, and the ratio of NY Mets fans to Boston Red Sox fans is 4:5.
# Hypothesis: In a certain town, the ratio of NY Yankees fans to NY Mets fans is 3:2, and the ratio of NY Mets fans to Boston Red Sox fans is 4:5.
# Golden Label: neutral

yankees_mets_ratio_premise = 4 / 2
yankees_mets_ratio_hypothesis = 3 / 2
mets_redsox_ratio_premise = 4 / 5
mets_redsox_ratio_hypothesis = 4 / 5

# the hypothesis refers to the same ratios between fans of different teams as the premise
if yankees_mets_ratio_hypothesis > yankees_mets_ratio_premise:
    # check if the hypothesized ratio of yankees to mets fans contradicts the premise
    label = "contradiction"
elif mets_redsox_ratio_hypothesis != mets_redsox_ratio_premise:
    # check if the hypothesized ratio of mets to red sox fans contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

