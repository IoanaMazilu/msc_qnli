people_own_pets_premise = 70
people_own_pets_hypothesis = 40

# the hypothesis talks about the number of people owning cats, dogs, or rabbits in a city, referenced also in the premise
if people_own_pets_hypothesis <= people_own_pets_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_own_pets_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people owning pets
    # any number of people owning pets greater than 'people_own_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
