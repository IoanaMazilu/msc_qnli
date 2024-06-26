AB_BC_ratio_premise = 2/3
AB_BC_ratio_hypothesis = 5/3

# the hypothesis is talking about the ratio of distances between A to B and B to C, referenced also in the premise
if AB_BC_ratio_hypothesis != AB_BC_ratio_premise:
    # check if the ratio value in the hypothesis contradicts the ratio value in the premise
    label = "contradiction"
else:
    # if the ratio values in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)
