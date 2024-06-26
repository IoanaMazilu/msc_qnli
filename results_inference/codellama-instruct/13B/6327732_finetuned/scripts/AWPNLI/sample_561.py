birds_in_tree_premise = 21.0
more_birds_flew_away_premise = 14.0
birds_left_in_tree_hypothesis = 6.0

# the hypothesis refers to the number of birds left in the tree, which is also mentioned in the premise
# compute the total number of birds in the premise
total_birds_premise = birds_in_tree_premise + more_birds_flew_away_premise
if birds_left_in_tree_hypothesis > total_birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
