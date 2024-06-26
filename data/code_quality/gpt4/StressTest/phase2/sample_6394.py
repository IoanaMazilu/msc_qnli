oil_per_cylinder_premise = 7
oil_per_cylinder_hypothesis = 8

# the hypothesis specifies the oil requirement for each cylinder in George's car, also referenced in the premise
if oil_per_cylinder_hypothesis <= oil_per_cylinder_premise:
    # check if the hypothesis value contradicts the requirement of more than 'oil_per_cylinder_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the oil requirement
    # any amount of oil greater than 'oil_per_cylinder_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
