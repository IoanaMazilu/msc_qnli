pet_owners_premise = 90
pet_owners_hypothesis = 10

# the hypothesis refers to the number of pet owners in San Durango mentioned in the premise
if pet_owners_premise <= pet_owners_hypothesis:
    # check if the estimate of 'pet_owners_hypothesis' contradicts the number of pet owners in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
