cylinder_oil_premise = 8
cylinder_oil_hypothesis = 7

# the hypothesis refers to the amount of oil needed for each cylinder used in the car
if cylinder_oil_hypothesis <= cylinder_oil_premise:
    # check if the hypothesis value contradicts the estimate of 'cylinder_oil_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of oil needed
    # any amount of oil greater than 'cylinder_oil_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
