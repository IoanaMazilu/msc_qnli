parrots_premise = 10
fishes_premise = 4
rabbits_premise = 9
dogs_premise = 6

parrots_hypothesis = 10
fishes_hypothesis = 4
rabbits_hypothesis = 9
dogs_hypothesis = 6

# the hypothesis refers to the number of each animal James have, mentioned in the premise
if parrots_hypothesis <= parrots_premise or fishes_hypothesis!= fishes_premise or rabbits_hypothesis!= rabbits_premise or dogs_hypothesis!= dogs_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives exact numbers for each animal
    # any number of animals greater than 'parrots_premise', 'fishes_premise', 'rabbits_premise', 'dogs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
