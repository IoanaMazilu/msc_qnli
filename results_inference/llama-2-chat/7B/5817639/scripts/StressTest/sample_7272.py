trees_premise = 12
trees_hypothesis = 72

# the hypothesis refers to the number of trees the lumberjack is supposed to cut down
if trees_hypothesis <= trees_premise:
    # check if the estimate of 'trees_hypothesis' contradicts the number of trees in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of trees
    # any number of trees greater than 'trees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
