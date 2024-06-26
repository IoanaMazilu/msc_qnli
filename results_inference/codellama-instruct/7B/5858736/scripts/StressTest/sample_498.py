shirts_premise = 1
pants_premise = 1
sneakers_premise = 1

shirts_hypothesis = 6
pants_hypothesis = 1
sneakers_hypothesis = 1

if shirts_premise <= shirts_hypothesis and pants_premise == pants_hypothesis and sneakers_premise == sneakers_hypothesis:
    label = "entailment"
elif shirts_premise > shirts_hypothesis or pants_premise!= pants_hypothesis or sneakers_premise!= sneakers_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
