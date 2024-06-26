puppies_premise = 2
puppies_hypothesis = 8
birds_premise = 9
birds_hypothesis = 9
fishes_premise = 4
fishes_hypothesis = 4

if puppies_hypothesis!= puppies_premise or birds_hypothesis!= birds_premise or fishes_hypothesis!= fishes_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
