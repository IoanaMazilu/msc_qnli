yankees_mets_ratio_premise = 3 / 2
yankees_mets_ratio_hypothesis = 3 / 2
mets_redsox_ratio_premise = 4 / 5
mets_redsox_ratio_hypothesis = 4 / 5

# the hypothesis talks about the ratios of NY Yankees fans to NY Mets fans and NY Mets fans to Boston Red Sox fans
if yankees_mets_ratio_hypothesis >= yankees_mets_ratio_premise:
    # check if the hypothesis value contradicts the premise value of 'yankees_mets_ratio_premise'
    label = "contradiction"
elif mets_redsox_ratio_hypothesis != mets_redsox_ratio_premise:
    # check if the ratio of NY Mets fans to Boston Red Sox fans in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
