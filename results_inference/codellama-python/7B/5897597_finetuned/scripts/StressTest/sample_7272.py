trees_to_cut_premise = 12
trees_to_cut_hypothesis = 72

# the hypothesis refers to the number of trees Kyle has to cut down, mentioned in the premise
if trees_to_cut_premise >= trees_to_cut_hypothesis:
    # check if the number of trees in the premise contradicts the estimate of less than 'trees_to_cut_hypothesis'
    label = "contradiction"
else:
    # if the number of trees in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
