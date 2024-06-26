fishes_caught_premise = 40
fishes_caught_hypothesis = 30

# the hypothesis refers to the number of fishes caught by Sony and Johnny mentioned in the premise
if fishes_caught_premise <= fishes_caught_hypothesis:
    # check if the estimate of 'fishes_caught_hypothesis' contradicts the number of fishes caught in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
