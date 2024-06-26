people_own_pets_premise = 50
people_own_pets_hypothesis = 50

# the hypothesis refers to the number of people in the city who own cats, dogs, or rabbits
if people_own_pets_hypothesis <= people_own_pets_premise:
    # check if the estimate of 'people_own_pets_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who own cats, dogs, or rabbits
    # any number of people greater than 'people_own_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
