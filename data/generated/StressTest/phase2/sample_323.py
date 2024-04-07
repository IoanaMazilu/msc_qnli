# Premise: Sony and Johnny caught 50 fishes.
# Hypothesis: Sony and Johnny caught 80 fishes.
# Golden Label: contradiction

fishes_caught_premise = 50
fishes_caught_hypothesis = 80

# the hypothesis talks about the number of fishes caught, which is also mentioned in the premise
if fishes_caught_hypothesis != fishes_caught_premise:
    # check if the number of fishes caught in the hypothesis contradicts the number of fishes caught in the premise
    label = "contradiction"
else:
    # if the number of fishes caught in the hypothesis doesn't contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

