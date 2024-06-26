birds_in_tree_premise = 21.0
birds_flew_away_premise = 14.0
birds_left_hypothesis = 6.0

# the hypothesis refers to the number of birds left in the tree, which can be computed from the premise
# compute the total number of birds left in the tree from the premise
birds_left_premise = birds_in_tree_premise - birds_flew_away_premise
if birds_left_hypothesis!= birds_left_premise:
    # check if the number of birds left in the hypothesis contradicts the number of birds left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
