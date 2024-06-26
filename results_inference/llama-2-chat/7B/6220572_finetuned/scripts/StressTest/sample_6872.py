puppies_premise = 2
puppies_hypothesis = 8
birds_premise = 9
birds_hypothesis = 9
fishes_premise = 4
fishes_hypothesis = 4

# the hypothesis refers to the number of puppies, birds, and fishes mentioned in the premise
if puppies_hypothesis == puppies_premise and birds_hypothesis == birds_premise and fishes_hypothesis == fishes_premise:
    # check if the hypothesis values contradict the premise ones
    label = "entailment"
elif puppies_hypothesis < puppies_premise or birds_hypothesis!= birds_premise or fishes_hypothesis!= fishes_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
