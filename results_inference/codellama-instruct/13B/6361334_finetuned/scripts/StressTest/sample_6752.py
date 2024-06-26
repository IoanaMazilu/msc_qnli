people_own_pets_premise = 50
people_own_pets_hypothesis = 50

# the hypothesis refers to the number of people owning cats, dogs, or rabbits in the city of San Durango
# mentioned in the premise
if people_own_pets_hypothesis <= people_own_pets_premise:
    # check if the estimate of 'people_own_pets_hypothesis' contradicts the number of people owning pets in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
