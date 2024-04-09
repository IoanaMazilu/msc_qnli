people_own_pets_premise = 40
people_own_pets_hypothesis = 70

# the hypothesis refers to the number of people owning cats, dogs, or rabbits in the premise city
if people_own_pets_premise <= people_own_pets_hypothesis:
    # check if the estimate of 'people_own_pets_hypothesis' contradicts the number of people owning pets in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people owning pets
    # any number of people owning pets less than 'people_own_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
