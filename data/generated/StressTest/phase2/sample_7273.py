# Premise: Kyle is a lumberjack with less than 72 trees to cut down.
# Hypothesis: Kyle is a lumberjack with 12 trees to cut down.
# Golden Label: neutral

trees_to_cut_premise = 72
trees_to_cut_hypothesis = 12

# the hypothesis refers to the number of trees to cut down mentioned in the premise
if trees_to_cut_hypothesis >= trees_to_cut_premise:
    # check if the hypothesis value contradicts the estimate of less than 'trees_to_cut_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of trees
    # any number of trees less than 'trees_to_cut_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

