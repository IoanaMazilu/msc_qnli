people_own_pets_premise = 70
people_own_pets_hypothesis = 50

# the hypothesis refers to the number of pet owners in San Durango mentioned in the premise
if people_own_pets_hypothesis >= people_own_pets_premise:
    # check if the estimate of 'people_own_pets_hypothesis' contradicts the number of pet owners in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
