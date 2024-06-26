people_owning_pets_premise = 70
people_owning_pets_hypothesis = 40

# the hypothesis talks about the number of people owning cats, dogs, or rabbits in San Durango, referenced also in the premise
if people_owning_pets_hypothesis >= people_owning_pets_premise:
    # check if the estimate of 'people_owning_pets_hypothesis' contradicts the number of people owning pets in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people owning pets
    # any number of people owning pets less than 'people_owning_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
