fishes_caught_premise = 60
fishes_caught_hypothesis = 30

# the hypothesis refers to the number of fishes caught by Sony and Johnny
if fishes_caught_hypothesis <= fishes_caught_premise:
    # check if the estimate of 'fishes_caught_hypothesis' contradicts the number of fishes caught in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fishes caught
    # any number of fishes greater than 'fishes_caught_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
