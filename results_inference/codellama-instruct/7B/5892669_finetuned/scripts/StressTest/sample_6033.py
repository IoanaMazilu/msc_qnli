pet_owners_premise = 40
pet_owners_hypothesis = 70

# the hypothesis refers to the number of pet owners in the premise
if pet_owners_premise >= pet_owners_hypothesis:
    # check if the number of pet owners in the premise contradicts the estimate of less than 'pet_owners_hypothesis'
    label = "contradiction"
else:
    # if the number of pet owners in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
