# Premise: In a certain town, the ratio of NY Yankees fans to NY Mets fans is 3:2, and the ratio of NY Mets fans to Boston Red Sox fans is 4:5.
# Hypothesis: In a certain town, the ratio of NY Yankees fans to NY Mets fans is less than 4:2, and the ratio of NY Mets fans to Boston Red Sox fans is 4:5.
# Golden Label: entailment

yankees_mets_ratio_premise = 3 / 2
yankees_mets_ratio_hypothesis = 4 / 2
mets_redsox_ratio_premise = 4 / 5
mets_redsox_ratio_hypothesis = 4 / 5

# the hypothesis refers to two ratios of sports fans mentioned in the premise
if yankees_mets_ratio_hypothesis >= yankees_mets_ratio_premise:
    # check if the ratio in 'yankees_mets_ratio_hypothesis' contradicts the ratio of fans in the premise
    label = "contradiction"
elif mets_redsox_ratio_hypothesis != mets_redsox_ratio_premise:
    # check if the ratio of Mets to Red Sox fans in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

