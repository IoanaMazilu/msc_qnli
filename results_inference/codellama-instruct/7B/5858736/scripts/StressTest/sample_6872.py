puppies_mary_premise = 2
birds_mary_premise = 9
fishes_mary_premise = 4

puppies_mary_hypothesis = 8
birds_mary_hypothesis = 9
fishes_mary_hypothesis = 4

if puppies_mary_hypothesis <= puppies_mary_premise:
    label = "contradiction"
elif birds_mary_hypothesis!= birds_mary_premise:
    label = "contradiction"
elif fishes_mary_hypothesis!= fishes_mary_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
