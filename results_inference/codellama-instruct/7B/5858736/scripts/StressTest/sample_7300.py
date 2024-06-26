parrots_james_premise = 70
parrots_james_hypothesis = 10
fishes_james_premise = 4
fishes_james_hypothesis = 4
rabbits_james_premise = 9
rabbits_james_hypothesis = 9
dogs_james_premise = 6
dogs_james_hypothesis = 6

# the hypothesis talks about the number of parrots, fishes, rabbits and dogs owned by James
if parrots_james_hypothesis <= parrots_james_premise:
    # check if the hypothesis value contradicts the estimate of less than 'parrots_james_premise'
    label = "contradiction"
elif fishes_james_hypothesis!= fishes_james_premise:
    # check if the number of fishes in the hypothesis contradicts the number of fishes reported in the premise
    label = "contradiction"
elif rabbits_james_hypothesis!= rabbits_james_premise:
    # check if the number of rabbits in the hypothesis contradicts the number of rabbits reported in the premise
    label = "contradiction"
elif dogs_james_hypothesis!= dogs_james_premise:
    # check if the number of dogs in the hypothesis contradicts the number of dogs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
