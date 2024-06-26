fishes_caught_premise = 75
fishes_caught_hypothesis = 15

# the hypothesis refers to the number of fish caught by Sony and Johnny mentioned in the premise
if fishes_caught_premise <= fishes_caught_hypothesis:
    # check if the estimate of 'fishes_caught_hypothesis' contradicts the number of fish caught in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
