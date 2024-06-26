oil_premise = 8
oil_hypothesis = 8

# the hypothesis refers to the amount of oil needed for George's car, mentioned in the premise
if oil_hypothesis <= oil_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact amount of oil needed for the car
    # any amount of oil greater than 'oil_premise' contradicts the premise
    label = "neutral"

print(label)
