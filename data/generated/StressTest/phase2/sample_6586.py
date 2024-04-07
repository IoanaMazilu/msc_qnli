# Premise: Sony and Johnny caught more than 40 fishes.
# Hypothesis: Sony and Johnny caught 60 fishes.
# Golden Label: neutral

fishes_caught_premise = 40
fishes_caught_hypothesis = 60

# the hypothesis refers to the number of fishes caught, which is also mentioned in the premise
if fishes_caught_hypothesis <= fishes_caught_premise:
    # check if the number of fishes in the hypothesis contradicts the premise's estimate of 'more than 40'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fishes
    # any number of fishes greater than 'fishes_caught_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

