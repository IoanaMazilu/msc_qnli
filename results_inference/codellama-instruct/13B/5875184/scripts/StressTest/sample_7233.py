premise_distance = 2
hypothesis_distance = 3

# the hypothesis refers to the distance run by the twins, which is less than the distance mentioned in the premise
if hypothesis_distance >= premise_distance:
    # check if the hypothesis value contradicts the estimate of less than 'premise_distance'
    label = "contradiction"
else:
    # the premise gives an estimate for the distance run by the twins
    # any distance less than 'premise_distance' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
