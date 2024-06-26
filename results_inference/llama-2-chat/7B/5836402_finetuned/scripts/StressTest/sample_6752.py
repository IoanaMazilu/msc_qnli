people_owning_pets_premise = 50
people_owning_pets_hypothesis = 50

# the hypothesis refers to the number of people owning pets mentioned in the premise
if people_owning_pets_hypothesis <= people_owning_pets_premise:
    # check if the estimate of 'people_owning_pets_hypothesis' contradicts the number of people owning pets in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
