yhat_premise = 2/3
yhat_hypothesis = 8/3

# the hypothesis talks about the ratio of distances between A to B and B to C, which is also mentioned in the premise
if yhat_hypothesis!= yhat_premise:
    # check if the ratio in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # if the ratios are the same, we can infer entailment
    label = "entailment"

print(label)
