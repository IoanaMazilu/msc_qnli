premise_distance = 3
hypothesis_distance = 2

# the hypothesis refers to a shorter distance than the premise
if hypothesis_distance < premise_distance:
    # check if the hypothesis value contradicts the estimate of less than 'premise_distance'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than or equal to 'premise_distance' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
