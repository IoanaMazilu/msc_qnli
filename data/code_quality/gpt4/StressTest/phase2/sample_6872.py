puppies_premise = 2
puppies_hypothesis = 8
birds_premise = 9
birds_hypothesis = 9
fishes_premise = 4
fishes_hypothesis = 4

# the hypothesis talks about the number of animals Mary has, which is also mentioned in the premise
if puppies_premise != puppies_hypothesis:
    # check if the number of puppies in the hypothesis contradicts the number of puppies reported in the premise
    label = "contradiction"
elif birds_premise != birds_hypothesis:
    # check if the number of birds in the hypothesis contradicts the number of birds reported in the premise
    label = "contradiction"
elif fishes_premise != fishes_hypothesis:
    # check if the number of fishes in the hypothesis contradicts the number of fishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
