oil_per_cylinder_premise = 8
oil_per_cylinder_hypothesis = 8

# the hypothesis refers to the amount of oil needed per cylinder, mentioned in the premise
if oil_per_cylinder_hypothesis <= oil_per_cylinder_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact number for the oil needed per cylinder
    # any number greater than 'oil_per_cylinder_premise' cannot be explicitly entailed from the premise, but does not contradict it either
    label = "neutral"

print(label)
