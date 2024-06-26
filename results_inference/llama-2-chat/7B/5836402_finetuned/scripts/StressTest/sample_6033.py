people_owning_pets_premise = 40
people_owning_pets_hypothesis = 70

# the hypothesis refers to the number of people owning pets in San Durango, which is also mentioned in the premise
if people_owning_pets_hypothesis >= people_owning_pets_premise:
    # check if the estimate of 'people_owning_pets_hypothesis' contradicts the number of people owning pets in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
