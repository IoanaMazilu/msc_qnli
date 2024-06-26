fishes_caught_premise = 75
fishes_caught_hypothesis = 75

# the hypothesis references the number of fishes caught by Sony and Johnny, mentioned in the premise
if fishes_caught_hypothesis >= fishes_caught_premise:
    # check if the hypothesis value contradicts the exact number of fishes caught in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of fishes caught
    # the hypothesis that Sony and Johnny caught more than 'fishes_caught_premise' contradicts this number
    label = "contradiction"

print(label)
