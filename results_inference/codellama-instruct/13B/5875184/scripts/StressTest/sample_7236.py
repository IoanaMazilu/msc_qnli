premise_distance = 240
hypothesis_distance = 440

# the hypothesis refers to the number of miles traveled on the first day of the vacation
if premise_distance < hypothesis_distance:
    # check if the estimate of 'hypothesis_distance' contradicts the number of miles traveled in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of miles traveled
    # any number of miles greater than 'premise_distance' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
