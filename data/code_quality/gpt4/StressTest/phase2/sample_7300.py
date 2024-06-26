parrots_premise = 70
parrots_hypothesis = 10
fishes_premise = 4
fishes_hypothesis = 4
rabbits_premise = 9
rabbits_hypothesis = 9
dogs_premise = 6
dogs_hypothesis = 6

# the hypothesis talks about James's pets, which are also referenced in the premise
if parrots_hypothesis >= parrots_premise:
    # check if the number of parrots in the hypothesis contradicts the premise of less than 'parrots_premise' parrots
    label = "contradiction"
elif fishes_hypothesis != fishes_premise or rabbits_hypothesis != rabbits_premise or dogs_hypothesis != dogs_premise:
    # check if the number of fishes, rabbits or dogs in the hypothesis contradicts the number of fishes, rabbits or dogs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
