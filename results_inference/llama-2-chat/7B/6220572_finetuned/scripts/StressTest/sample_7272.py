trees_cut_down_premise = 12
trees_cut_down_hypothesis = 72

# the hypothesis refers to the number of trees to cut down, also mentioned in the premise
if trees_cut_down_hypothesis >= trees_cut_down_premise:
    # check if the estimate of 'trees_cut_down_hypothesis' contradicts the number of trees to cut down in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of trees to cut down
    # any number of trees to cut down less than 'trees_cut_down_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
