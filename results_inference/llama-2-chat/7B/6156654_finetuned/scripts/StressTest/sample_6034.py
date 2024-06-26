people_owning_pets_premise = 70
people_owning_pets_hypothesis = 40

# the hypothesis refers to the number of people owning cats, dogs, or rabbits in the city of San Durango, which is also mentioned in the premise
if people_owning_pets_hypothesis >= people_owning_pets_premise:
    # check if the number of people owning pets in the hypothesis contradicts the premise
    label = "contradiction"
elif people_owning_pets_hypothesis < people_owning_pets_premise:
    # if the number of people owning pets in the hypothesis is less than the premise, it is consistent with the premise, but cannot be explicitly entailed
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it is consistent with the premise, but cannot be explicitly entailed
    label = "neutral"

print(label)
