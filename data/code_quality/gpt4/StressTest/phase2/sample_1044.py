pet_owners_premise = 60
pet_owners_hypothesis = 50

# the hypothesis refers to the number of pet owners in the city of San Durango mentioned in the premise
if pet_owners_premise < pet_owners_hypothesis:
    # check if the number of 'pet_owners_hypothesis' contradicts the number of pet owners in the premise
    label = "contradiction"
elif pet_owners_premise == pet_owners_hypothesis:
    # check if the number of 'pet_owners_hypothesis' contradicts the premise of more than 'pet_owners_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
