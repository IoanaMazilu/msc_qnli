parrots_premise = 10
fishes_premise = 4
rabbits_premise = 9
dogs_premise = 6

# the hypothesis talks about the number of animals owned by James, referenced also in the premise
if parrots_hypothesis > parrots_premise:
    # check if the hypothesis value contradicts the estimate of 'parrots_premise'
    label = "contradiction"
elif fishes_hypothesis > fishes_premise or rabbits_hypothesis > rabbits_premise or dogs_hypothesis > dogs_premise:
    # check if any aspect of the hypothesis contradicts any aspect of the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
