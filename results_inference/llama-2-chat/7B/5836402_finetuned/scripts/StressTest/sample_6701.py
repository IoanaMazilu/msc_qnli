share_premise = 4500
share_hypothesis = 7500

# the hypothesis talks about the share of Tony, referenced also in the premise
if share_hypothesis!= share_premise:
    # check if the share in the hypothesis contradicts the share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
