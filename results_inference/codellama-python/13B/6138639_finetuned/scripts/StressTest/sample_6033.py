pets_owners_premise = 40
pets_owners_hypothesis = 70

# the hypothesis refers to the number of pet owners in San Durango mentioned in the premise
if pets_owners_premise >= pets_owners_hypothesis:
    # check if the number of pet owners in the premise contradicts the estimate of less than 'pets_owners_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
