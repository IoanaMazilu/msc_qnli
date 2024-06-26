fine_premise = 14
fine_hypothesis = 14

# the hypothesis and premise mention the fine amount
if fine_premise!= fine_hypothesis:
    # check if the fine amount in the hypothesis contradicts the fine amount in the premise
    label = "contradiction"
else:
    # if the fine amount in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
