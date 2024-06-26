parrots_premise = 10
parrots_hypothesis = 70
fishes_premise = 4
fishes_hypothesis = 4
rabbits_premise = 9
rabbits_hypothesis = 9
dogs_premise = 6
dogs_hypothesis = 6

# the hypothesis refers to the number of pets James have, mentioned in the premise
if parrots_premise >= parrots_hypothesis:
    # check if the estimate of 'parrots_hypothesis' contradicts the number of parrots in the premise
    label = "contradiction"
elif fishes_hypothesis!= fishes_premise or rabbits_hypothesis!= rabbits_premise or dogs_hypothesis!= dogs_premise:
    # check if the number of each pet in the hypothesis contradicts the number of each pet reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
