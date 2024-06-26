ratio_premise = 2/3
ratio_hypothesis = 8/3

# the hypothesis talks about the ratio of distances between A to B and B to C, which is also referenced in the premise
if ratio_premise!= ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratios are the same, we can infer entailment
    label = "entailment"

print(label)
