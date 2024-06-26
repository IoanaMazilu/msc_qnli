shirt_outfit_premise = 1
jeans_outfit_premise = 1
sneakers_outfit_premise = 1

shirt_hypothesis = 8
jeans_hypothesis = 1
sneakers_hypothesis = 1

if shirt_outfit_premise <= shirt_hypothesis and jeans_outfit_premise <= jeans_hypothesis and sneakers_outfit_premise <= sneakers_hypothesis:
    label = "entailment"
else:
    label = "contradiction"

print(label)
