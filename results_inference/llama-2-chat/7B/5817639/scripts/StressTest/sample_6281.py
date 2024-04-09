ratio_premise = 7
ratio_hypothesis = 5

# the hypothesis talks about the ratio of question submitters, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, and the hypothesis value is consistent with it
    label = "entailment"

print(label)
