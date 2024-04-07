# Premise: In a certain town, the ratio of NY Yankees fans to NY Mets fans is more than 1:1, and the ratio of NY Mets fans to Boston Red Sox fans is 3:7.
# Hypothesis: In a certain town, the ratio of NY Yankees fans to NY Mets fans is 2:1, and the ratio of NY Mets fans to Boston Red Sox fans is 3:7.
# Golden Label: neutral

yankees_mets_ratio_premise = 1
yankees_mets_ratio_hypothesis = 2
mets_redsox_ratio_premise = 3/7
mets_redsox_ratio_hypothesis = 3/7

# the hypothesis refers to the ratio of fans in the town mentioned in the premise
if yankees_mets_ratio_hypothesis <= yankees_mets_ratio_premise:
    # check if the estimate of 'yankees_mets_ratio_hypothesis' contradicts the ratio of fans in the premise
    label = "contradiction"
elif mets_redsox_ratio_hypothesis != mets_redsox_ratio_premise:
    # check if the ratio of Mets fans to Red Sox fans in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
elif yankees_mets_ratio_hypothesis > yankees_mets_ratio_premise:
    # the premise gives only a minimum estimate for the ratio of Yankees fans to Mets fans
    # any ratio greater than 'yankees_mets_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

