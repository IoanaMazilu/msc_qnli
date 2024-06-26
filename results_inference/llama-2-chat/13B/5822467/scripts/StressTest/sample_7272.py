kyle_trees_premise = 12
kyle_trees_hypothesis = 72

# the hypothesis refers to the number of trees Kyle has to cut down
if kyle_trees_hypothesis <= kyle_trees_premise:
    # check if the hypothesis value contradicts the estimate of 'kyle_trees_premise'
    label = "contradiction"
elif kyle_trees_premise > kyle_trees_hypothesis:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the number of trees
    # any number of trees less than 'kyle_trees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
