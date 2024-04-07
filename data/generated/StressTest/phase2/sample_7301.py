# Premise: James have 10 parrots, 4 fishes, 9 rabbits and 6 dogs.
# Hypothesis: James have more than 10 parrots, 4 fishes, 9 rabbits and 6 dogs.
# Golden Label: contradiction

parrots_premise = 10
fishes_premise = 4
rabbits_premise = 9
dogs_premise = 6

parrots_hypothesis = 10
fishes_hypothesis = 4
rabbits_hypothesis = 9
dogs_hypothesis = 6

# the hypothesis refers to the number of parrots, fishes, rabbits and dogs mentioned in the premise
if parrots_hypothesis > parrots_premise:
    # check if the estimate of 'parrots_hypothesis' contradicts the number of parrots in the premise
    label = "contradiction"
elif fishes_hypothesis != fishes_premise or rabbits_hypothesis != rabbits_premise or dogs_hypothesis != dogs_premise:
    # check if the number of fishes, rabbits and dogs in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but they can't be explicitly entailed from the premise
    label = "neutral"

print(label)

