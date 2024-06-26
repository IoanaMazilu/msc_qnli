total_pets_premise = 96
total_pets_hypothesis = 56

# the hypothesis refers to the total number of pets Claire has, which is also mentioned in the premise
if total_pets_premise <= total_pets_hypothesis:
    # check if the estimate of 'total_pets_hypothesis' contradicts the number of pets in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
