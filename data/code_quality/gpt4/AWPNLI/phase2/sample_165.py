birds_in_tree_premise = 14.0
birds_flew_premise = 21.0
total_birds_hypothesis = 39.0

# the hypothesis refers to the total number of birds in the tree, which are also mentioned in the premise
# compute the total number of birds in the premise
total_birds_premise = birds_in_tree_premise + birds_flew_premise
if total_birds_hypothesis != total_birds_premise:
    # check if the total number of birds in the hypothesis contradicts the total number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
