# Premise: 21.0 birds were sitting in a tree and 14.0 more birds flew away.
# Hypothesis: 7.0 birds are left in the tree.
# Golden Label: entailment

birds_in_tree_premise = 21.0
birds_flew_away_premise = 14.0
birds_left_hypothesis = 7.0

# the hypothesis refers to the number of birds left in the tree, which can be derived from the premise
# compute the number of birds left in the tree in the premise
birds_left_premise = birds_in_tree_premise - birds_flew_away_premise
if birds_left_hypothesis != birds_left_premise:
    # check if the number of birds left in the hypothesis contradicts the number of birds left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
