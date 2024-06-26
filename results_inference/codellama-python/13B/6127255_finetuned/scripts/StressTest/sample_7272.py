trees_to_cut_premise = 12
trees_to_cut_hypothesis = 72

# the hypothesis refers to the number of trees to cut down mentioned in the premise
if trees_to_cut_premise >= trees_to_cut_hypothesis:
    # check if the number of trees to cut down in the premise contradicts the estimate of less than 'trees_to_cut_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
