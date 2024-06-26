parrots_premise = 10
parrots_hypothesis = 70
fishes_premise = 4
fishes_hypothesis = 4
rabbits_premise = 9
rabbits_hypothesis = 9
dogs_premise = 6
dogs_hypothesis = 6

# the hypothesis talks about the number of animals James has, all also referenced in the premise
if parrots_premise > parrots_hypothesis:
    # check if the number of parrots in the premise contradicts the estimate of less than 'parrots_hypothesis'
    label = "contradiction"
elif fishes_premise != fishes_hypothesis:
    # check if the number of fishes in the premise contradicts the number of fishes in the hypothesis
    label = "contradiction"
elif rabbits_premise != rabbits_hypothesis:
    # check if the number of rabbits in the premise contradicts the number of rabbits in the hypothesis
    label = "contradiction"
elif dogs_premise != dogs_hypothesis:
    # check if the number of dogs in the premise contradicts the number of dogs in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
