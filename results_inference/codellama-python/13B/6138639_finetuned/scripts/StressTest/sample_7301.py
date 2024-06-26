parrots_premise = 10
parrots_hypothesis = 10
fishes_premise = 4
fishes_hypothesis = 4
rabbits_premise = 9
rabbits_hypothesis = 9
dogs_premise = 6
dogs_hypothesis = 6

# the hypothesis talks about the number of pets James have, referenced also in the premise
if parrots_hypothesis <= parrots_premise:
    # check if the hypothesis value contradicts the estimate of more than 'parrots_premise'
    label = "contradiction"
elif fishes_hypothesis!= fishes_premise:
    # check if the number of fishes in the hypothesis contradicts the number of fishes reported in the premise
    label = "contradiction"
elif rabbits_hypothesis!= rabbits_premise:
    # check if the number of rabbits in the hypothesis contradicts the number of rabbits reported in the premise
    label = "contradiction"
elif dogs_hypothesis!= dogs_premise:
    # check if the number of dogs in the hypothesis contradicts the number of dogs reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of parrots
    # any number of parrots greater than 'parrots_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
