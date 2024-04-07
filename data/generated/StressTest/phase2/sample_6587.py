# Premise: Sony and Johnny caught 60 fishes.
# Hypothesis: Sony and Johnny caught 30 fishes.
# Golden Label: contradiction

fishes_caught_premise = 60
fishes_caught_hypothesis = 30

# the hypothesis refers to the number of fishes caught by Sony and Johnny, which is also mentioned in the premise
if fishes_caught_premise != fishes_caught_hypothesis:
    # check if the number of fishes caught in the hypothesis contradicts the number of fishes caught in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

