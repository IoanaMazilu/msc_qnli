puppies_premise = 2
puppies_hypothesis = 8
birds_premise = 9
birds_hypothesis = 9
fishes_premise = 4
fishes_hypothesis = 4

# the hypothesis refers to the number of puppies, birds and fishes that Mary has, as mentioned in the premise
if puppies_hypothesis!= puppies_premise:
    # check if the number of puppies in the hypothesis contradicts the number of puppies reported in the premise
    label = "contradiction"
elif birds_hypothesis!= birds_premise or fishes_hypothesis!= fishes_premise:
    # check if the number of birds or fishes in the hypothesis contradicts the number of birds or fishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
