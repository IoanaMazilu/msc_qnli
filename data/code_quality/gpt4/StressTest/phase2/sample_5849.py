fishes_caught_premise = 25
fishes_caught_hypothesis = 15

# the hypothesis refers to the number of fishes Sony and Johnny caught, mentioned in the premise
if fishes_caught_hypothesis == fishes_caught_premise:
    # check if the hypothesis value is equal to the number of fishes caught in the premise
    label = "entailment"
elif fishes_caught_hypothesis > fishes_caught_premise:
    # check if the number of fishes caught in the hypothesis contradicts the number of fishes caught in the premise
    label = "contradiction"
else:
    # the hypothesis value is less than the premise value, but it doesn't contradict the premise
    # as it's possible they caught 15 out of 25 fishes
    label = "neutral" 

print(label)
