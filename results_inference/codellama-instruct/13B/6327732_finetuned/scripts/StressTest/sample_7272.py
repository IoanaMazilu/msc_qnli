trees_to_cut_premise = 12
trees_to_cut_hypothesis = 72

# the hypothesis refers to the number of trees to cut down mentioned in the premise
if trees_to_cut_hypothesis >= trees_to_cut_premise:
    # check if the estimate of 'trees_to_cut_hypothesis' contradicts the number of trees to cut down in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of trees to cut down
    # any number of trees less than 'trees_to_cut_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
