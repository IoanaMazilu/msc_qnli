parrots_premise = 10
parrots_hypothesis = 70
fishes_premise = 4
fishes_hypothesis = 4
rabbits_premise = 9
rabbits_hypothesis = 9
dogs_premise = 6
dogs_hypothesis = 6

# the hypothesis talks about the number of animals James owns, referenced also in the premise
if parrots_hypothesis <= parrots_premise:
    # check if the hypothesis value contradicts the estimate of 'parrots_premise'
    label = "contradiction"
elif fishes_hypothesis!= fishes_premise or rabbits_hypothesis!= rabbits_premise or dogs_hypothesis!= dogs_premise:
    # check if the number of animals in the hypothesis contradicts the number of animals reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
