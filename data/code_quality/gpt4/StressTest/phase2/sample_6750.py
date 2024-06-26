pet_owners_premise = 50
pet_owners_hypothesis = 70

# the hypothesis refers to the number of pet owners mentioned in the premise
if pet_owners_premise > pet_owners_hypothesis:
    # check if the number of pet owners in the premise contradicts the estimate of less than 'pet_owners_hypothesis'
    label = "contradiction"
elif pet_owners_premise == pet_owners_hypothesis:
    # check if the number of pet owners in the premise contradicts the estimate of less than 'pet_owners_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
