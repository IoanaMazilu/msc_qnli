sita_geeta_premise = 2
sita_geeta_hypothesis = 3

# the premise states that the twins ran for 2 km each
if sita_geeta_hypothesis <= sita_geeta_premise:
    # check if the hypothesis value contradicts the estimate of'sita_geeta_premise'
    label = "contradiction"
elif sita_geeta_hypothesis > 2:
    # check if the hypothesis value contradicts the estimate of'sita_geeta_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance ran
    # any distance less than or equal to 3 km is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
