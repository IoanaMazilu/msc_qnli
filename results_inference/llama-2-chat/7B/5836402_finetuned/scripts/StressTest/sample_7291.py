share_premise = 500
share_hypothesis = 600

# the hypothesis talks about Greg's share, which is also mentioned in the premise
if share_hypothesis!= share_premise:
    # check if the value of Greg's share in the hypothesis contradicts the value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
