pet_owners_premise = 40
pet_owners_hypothesis = 70

# the hypothesis refers to the number of pet owners in San Durango mentioned in the premise
if pet_owners_premise >= pet_owners_hypothesis:
    # check if the estimate of 'pet_owners_hypothesis' contradicts the number of pet owners in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)