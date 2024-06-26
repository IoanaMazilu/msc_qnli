# define the number of pets in the premise and hypothesis
pets_premise = 96
pets_hypothesis = 56

# the hypothesis refers to the number of pets mentioned in the premise
if pets_premise <= pets_hypothesis:
    # check if the estimate of 'pets_hypothesis' contradicts the number of pets in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)