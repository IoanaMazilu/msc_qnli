fishes_caught_premise = 60
fishes_caught_hypothesis = 30

# the hypothesis refers to the number of fishes caught by Sony and Johnny mentioned in the premise
if fishes_caught_hypothesis!= fishes_caught_premise:
    # check if the number of fishes caught in the hypothesis contradicts the number of fishes caught reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
