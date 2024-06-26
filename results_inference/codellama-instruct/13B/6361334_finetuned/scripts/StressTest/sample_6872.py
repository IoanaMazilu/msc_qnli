puppies_premise = 2
puppies_hypothesis = 8
birds_premise = 9
birds_hypothesis = 9
fishes_premise = 4
fishes_hypothesis = 4

# the hypothesis refers to the number of puppies, birds, and fishes mentioned in the premise
if puppies_premise <= puppies_hypothesis:
    # check if the estimate of 'puppies_hypothesis' contradicts the number of puppies in the premise
    label = "contradiction"
elif birds_hypothesis!= birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds reported in the premise
    label = "contradiction"
elif fishes_hypothesis!= fishes_premise:
    # check if the number of fishes in the hypothesis contradicts the number of fishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
