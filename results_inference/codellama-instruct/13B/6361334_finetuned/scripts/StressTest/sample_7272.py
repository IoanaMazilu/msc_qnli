trees_to_cut_premise = 12
trees_to_cut_hypothesis = 72

# the hypothesis refers to the number of trees to cut down mentioned in the premise
if trees_to_cut_hypothesis >= trees_to_cut_premise:
    # check if the estimate of 'trees_to_cut_hypothesis' contradicts the number of trees to cut down in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
