pet_owners_premise = 50
pet_owners_hypothesis = 50

# the hypothesis refers to the number of pet owners in the premise
if pet_owners_hypothesis >= pet_owners_premise:
    # check if the hypothesis value contradicts the exact number of pet owners in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
