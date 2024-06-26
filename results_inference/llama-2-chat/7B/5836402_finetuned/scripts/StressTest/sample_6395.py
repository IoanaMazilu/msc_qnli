oil_each_cylinder_premise = 8
oil_each_cylinder_hypothesis = 8

# the hypothesis refers to the amount of oil needed for each cylinder of George's car mentioned in the premise
if oil_each_cylinder_hypothesis <= oil_each_cylinder_premise:
    # check if the hypothesis value contradicts the estimate of 'oil_each_cylinder_premise'
    label = "contradiction"
else:
    # if the hypothesis value is greater than 'oil_each_cylinder_premise', it is not possible to explicitly entail it from the premise
    label = "neutral"

print(label)
