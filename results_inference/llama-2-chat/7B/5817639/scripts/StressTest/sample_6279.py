ratio_premise = 7
ratio_hypothesis = 8

# the hypothesis talks about the ratio of question submission, which is also mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, and the hypothesis value is consistent with it, so we can infer entailment
    label = "entailment"

print(label)
