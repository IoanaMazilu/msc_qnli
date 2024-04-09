sita_geeta_premise = 52
sita_geeta_hypothesis = 12

# the premise mentions the distance each twin ran as less than 52 km
if sita_geeta_hypothesis <= sita_geeta_premise:
    # check if the hypothesis value contradicts the estimate of'sita_geeta_premise'
    label = "contradiction"
elif sita_geeta_hypothesis > sita_geeta_premise:
    # the hypothesis value is greater than the estimate in the premise, so we can infer entailment
    label = "entailment"
else:
    # the premise only gives an estimate for the distance each twin ran
    # any distance less than 52 km is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
