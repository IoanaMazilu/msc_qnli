people_own_pets_premise = 40
people_own_pets_hypothesis = 70

# the hypothesis refers to the number of people in the city who own cats, dogs, or rabbits
if people_own_pets_hypothesis >= people_own_pets_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of people who own pets
    # any number of people less than 'people_own_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
