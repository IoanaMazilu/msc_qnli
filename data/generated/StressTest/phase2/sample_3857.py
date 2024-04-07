# Premise: Sony and Johnny caught 80 fishes.
# Hypothesis: Sony and Johnny caught 20 fishes.
# Golden Label: contradiction

fishes_caught_premise = 80
fishes_caught_hypothesis = 20

# the hypothesis refers to the number of fishes caught by Sony and Johnny, mentioned in the premise
if fishes_caught_premise == fishes_caught_hypothesis:
    # check if the number of fishes caught in the hypothesis is the same as the premise
    label = "entailment"
elif fishes_caught_hypothesis < fishes_caught_premise:
    # check if the number of fishes caught in the hypothesis contradicts the number of fishes caught in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we could infer neutrality
    label = "neutral"

print(label)

