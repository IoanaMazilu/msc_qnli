# Premise: Sony and Johnny caught 40 fishes.
# Hypothesis: Sony and Johnny caught 50 fishes.
# Golden Label: contradiction

fishes_caught_premise = 40
fishes_caught_hypothesis = 50

# the hypothesis refers to the same event of catching fishes as in the premise
if fishes_caught_hypothesis != fishes_caught_premise:
    # check if the number of fishes caught in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of fishes caught in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

