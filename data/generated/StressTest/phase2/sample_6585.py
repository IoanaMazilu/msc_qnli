# Premise: Sony and Johnny caught 60 fishes.
# Hypothesis: Sony and Johnny caught more than 40 fishes.
# Golden Label: entailment

fishes_premise = 60
fishes_hypothesis = 40

# the hypothesis refers to the number of fishes caught by Sony and Johnny, also mentioned in the premise
if fishes_premise <= fishes_hypothesis:
    # check if the hypothesis estimate contradicts the exact number of fishes in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate is not greater than the premise, we can infer entailment
    label = "entailment"

print(label)

