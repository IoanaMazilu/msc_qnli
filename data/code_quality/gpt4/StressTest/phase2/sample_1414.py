pet_owners_premise = 80
pet_owners_hypothesis = 60

# the hypothesis refers to the number of people in San Durango who own pets mentioned in the premise
if pet_owners_hypothesis >= pet_owners_premise:
    # check if the number of pet owners in the hypothesis contradicts the estimate of less than 'pet_owners_premise'
    label = "contradiction"
else:
    # if the hypothesis number of pet owners does not contradict the premise estimate, we can infer entailment
    label = "entailment"

print(label)
