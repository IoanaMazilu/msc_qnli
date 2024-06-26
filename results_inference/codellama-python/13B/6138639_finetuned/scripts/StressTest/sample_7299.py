parrots_premise = 10
parrots_hypothesis = 70
fishes_premise = 4
fishes_hypothesis = 4
rabbits_premise = 9
rabbits_hypothesis = 9
dogs_premise = 6
dogs_hypothesis = 6

# the hypothesis talks about the number of pets James have, referenced also in the premise
if parrots_premise >= parrots_hypothesis:
    # check if the number of parrots in the premise contradicts the estimate of less than 'parrots_hypothesis'
    label = "contradiction"
elif fishes_premise!= fishes_hypothesis or rabbits_premise!= rabbits_hypothesis or dogs_premise!= dogs_hypothesis:
    # check if the number of fishes, rabbits or dogs in the premise contradicts the number of fishes, rabbits or dogs in the hypothesis
    label = "contradiction"
else:
    # the premise gives exact number of pets
    # any number of pets less than 'parrots_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
