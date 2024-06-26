owners_animals_premise = 70
owners_animals_hypothesis = 40

# the hypothesis refers to the number of people owning cats, dogs, or rabbits in San Durango, which is also mentioned in the premise
if owners_animals_hypothesis >= owners_animals_premise:
    # check if the estimate of 'owners_animals_hypothesis' contradicts the number of owners of animals in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
