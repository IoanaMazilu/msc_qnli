parrots_premise = 70
parrots_hypothesis = 10
fishes_premise = 4
fishes_hypothesis = 4
rabbits_premise = 9
rabbits_hypothesis = 9
dogs_premise = 6
dogs_hypothesis = 6

# the hypothesis talks about the number of pets James have, referenced also in the premise
if parrots_hypothesis >= parrots_premise:
    # check if the hypothesis value contradicts the estimate of less than 'parrots_premise'
    label = "contradiction"
elif fishes_hypothesis!= fishes_premise or rabbits_hypothesis!= rabbits_premise or dogs_hypothesis!= dogs_premise:
    # check if the number of pets in the hypothesis contradicts the number of pets reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of parrots
    # any number of parrots less than 'parrots_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
