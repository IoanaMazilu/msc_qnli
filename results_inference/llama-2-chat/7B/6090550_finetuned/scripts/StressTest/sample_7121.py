 ratio_premise = 3/2
ratio_hypothesis = 8/2

# the hypothesis talks about the ratio of car and AC prices, referenced also in the premise
if ratio_hypothesis!= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # if the ratios are equal, we can infer entailment
    label = "entailment"

print(label)
