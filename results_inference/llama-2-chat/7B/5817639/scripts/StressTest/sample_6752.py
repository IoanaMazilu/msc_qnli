people_own_pets_premise = 50
people_own_pets_hypothesis = 50

# the premise and hypothesis refer to the number of people owning pets in San Durango
if people_own_pets_hypothesis <= people_own_pets_premise:
    # check if the hypothesis value contradicts the estimate of 'people_own_pets_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people owning pets,
    # any number of people owning pets greater than 'people_own_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
