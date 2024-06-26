initial_trees_premise = 13.0
planted_trees_premise = 12.0
total_trees_hypothesis = 28.0

# the hypothesis refers to the number of trees in the future, which can be computed from the premise
# compute the total number of trees in the premise
total_trees_premise = initial_trees_premise + planted_trees_premise
if total_trees_hypothesis != total_trees_premise:
    # check if the number of trees in the hypothesis contradicts the number of trees from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
