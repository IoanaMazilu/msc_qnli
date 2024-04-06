# Premise: 42.0 birds were sitting in a tree and then 29.0 more flew up to the tree.
# Hypothesis: 75.0 birds are there in the tree.
# Golden Label: contradiction

birds_sitting_tree_premise = 42.0
birds_flew_tree_premise = 29.0
total_birds_hypothesis = 75.0

# the hypothesis refers to the total number of birds in the tree, which is also calculated in the premise
# compute the total number of birds in the premise
total_birds_premise = birds_sitting_tree_premise + birds_flew_tree_premise
if total_birds_hypothesis != total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

