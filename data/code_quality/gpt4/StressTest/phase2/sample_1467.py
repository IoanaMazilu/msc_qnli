total_pets_premise = 86
total_pets_hypothesis = 76

# the hypothesis discusses the number of pets, similarly mentioned in the premise
if total_pets_premise <= total_pets_hypothesis:
    # check if the actual number of pets contradicts the hypothesis estimate of more than 'total_pets_hypothesis'
    label = "contradiction"
elif total_pets_premise > total_pets_hypothesis:
    # if the premise count is greater than the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
