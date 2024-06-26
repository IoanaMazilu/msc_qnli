pet_owners_premise = 40
pet_owners_hypothesis = 70

# The hypothesis refers to the number of pet owners in San Durango mentioned in the premise
if pet_owners_premise > pet_owners_hypothesis:
    # Check if the number of pet owners in the premise contradicts the hypothesis estimate of less than 'pet_owners_hypothesis'
    label = "contradiction"
elif pet_owners_premise == pet_owners_hypothesis:
    # Check if the number of pet owners in the premise is exactly the same as the hypothesis, which contradicts the 'less than' condition in the hypothesis
    label = "contradiction"
else:
    # If the number of pet owners in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
