sameer_share_premise = 6970
sameer_share_hypothesis = 5970

# the hypothesis is asking about the share of Sameer in the profit, which is also mentioned in the premise
if sameer_share_hypothesis != sameer_share_premise:
    # check if the share of Sameer in the hypothesis contradicts the share of Sameer in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
