kittens_born_premise = 8.0
kittens_given_premise = 2.0
kittens_remaining_hypothesis = 4.0

# the hypothesis refers to the number of kittens left, which can be calculated from the premise
# compute the number of kittens left in the premise
kittens_remaining_premise = kittens_born_premise - kittens_given_premise
if kittens_remaining_hypothesis != kittens_remaining_premise:
    # check if the number of kittens in the hypothesis contradicts the number of kittens remaining in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
