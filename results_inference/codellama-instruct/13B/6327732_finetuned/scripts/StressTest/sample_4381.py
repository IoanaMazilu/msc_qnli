premise_distance = 8 * 50
hypothesis_distance = 1 * 50

if premise_distance < hypothesis_distance:
    # check if the hypothesis value contradicts the estimate of less than 'premise_distance'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'premise_distance' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
