parrots_premise = 70 - 10
fishes_premise = 4
rabbits_premise = 9
dogs_premise = 6

parrots_hypothesis = 10
fishes_hypothesis = 4
rabbits_hypothesis = 9
dogs_hypothesis = 6

# check if the hypothesis values contradict the premise ones
if parrots_hypothesis > parrots_premise:
    label = "contradiction"
elif fishes_hypothesis!= fishes_premise:
    label = "contradiction"
elif rabbits_hypothesis!= rabbits_premise:
    label = "contradiction"
elif dogs_hypothesis!= dogs_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
