parrots_premise = 10
parrots_hypothesis = 10
fishes_premise = 4
fishes_hypothesis = 4
rabbits_premise = 9
rabbits_hypothesis = 9
dogs_premise = 6
dogs_hypothesis = 6

# the hypothesis refers to the number of parrots mentioned in the premise
if parrots_hypothesis <= parrots_premise:
    # check if the estimate of 'parrots_hypothesis' contradicts the number of parrots in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
