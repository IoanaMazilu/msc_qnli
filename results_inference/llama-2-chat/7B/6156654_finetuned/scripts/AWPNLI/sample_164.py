birds_premise = 14.0
birds_fly_premise = 21.0
birds_hypothesis = 35.0

# the hypothesis refers to the total number of birds in the tree, which can be computed from the premise
# the premise gives the number of birds that were sitting in the tree and the number of birds that flew up to the tree
# the hypothesis provides an estimate for the total number of birds in the tree

if birds_hypothesis!= birds_premise + birds_fly_premise:
    # check if the total number of birds in the hypothesis contradicts the total number of birds in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
