yankees_to_mets_premise = 3/2
yankees_to_mets_hypothesis = 8/2
mets_to_redsox_premise = 4/5
mets_to_redsox_hypothesis = 4/5

# the hypothesis talks about the ratios of fans of different teams mentioned in the premise
if yankees_to_mets_hypothesis >= yankees_to_mets_premise:
    # check if the hypothesis ratio of Yankees fans to Mets fans contradicts the ratio in the premise
    label = "contradiction"
elif mets_to_redsox_hypothesis != mets_to_redsox_premise:
    # check if the hypothesis ratio of Mets fans to Red Sox fans contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
