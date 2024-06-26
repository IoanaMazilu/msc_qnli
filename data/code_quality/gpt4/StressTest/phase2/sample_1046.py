pet_owners_premise = 60
pet_owners_hypothesis = 60

# the hypothesis refers to the number of pet owners in the city of San Durango, mentioned in the premise
if pet_owners_hypothesis < pet_owners_premise:
    # check if the hypothesis value contradicts the number of pet owners reported in the premise
    label = "contradiction"
elif pet_owners_hypothesis > pet_owners_premise:
    # check if the hypothesis value contradicts the number of pet owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
