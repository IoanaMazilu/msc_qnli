puppies_premise = 2
birds_premise = 9
fishes_premise = 4

# the hypothesis gives an estimate for the number of puppies
if puppies_premise >= 5:
    # check if the number of puppies in the hypothesis contradicts the exact number of puppies reported in the premise
    label = "contradiction"
elif birds_premise!= birds_hypothesis:
    # check if the number of birds in the hypothesis contradicts the number of birds reported in the premise
    label = "contradiction"
elif fishes_premise!= fishes_hypothesis:
    # check if the number of fishes in the hypothesis contradicts the number of fishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
