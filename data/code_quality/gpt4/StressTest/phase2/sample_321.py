fishes_caught_premise = 50
fishes_caught_hypothesis = 70

# the hypothesis refers to the number of fishes caught mentioned in the premise
if fishes_caught_hypothesis <= fishes_caught_premise:
    # check if the estimate of 'fishes_caught_hypothesis' contradicts the number of fishes caught in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
