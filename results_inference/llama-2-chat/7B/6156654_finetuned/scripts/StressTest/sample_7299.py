parrots_premise = 10
parrots_hypothesis = 70
fishes_premise = 4
fishes_hypothesis = 4
rabbits_premise = 9
rabbits_hypothesis = 9
dogs_premise = 6
dogs_hypothesis = 6

# the hypothesis refers to the number of each pet in James' collection
if parrots_hypothesis <= parrots_premise:
    # check if the number of parrots in the hypothesis contradicts the number of parrots in the premise
    label = "contradiction"
elif fishes_hypothesis!= fishes_premise:
    # check if the number of fishes in the hypothesis contradicts the number of fishes in the premise
    label = "contradiction"
elif rabbits_hypothesis!= rabbits_premise:
    # check if the number of rabbits in the hypothesis contradicts the number of rabbits in the premise
    label = "contradiction"
elif dogs_hypothesis!= dogs_premise:
    # check if the number of dogs in the hypothesis contradicts the number of dogs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values
    # then we can infer entailment
    label = "entailment"

print(label)
