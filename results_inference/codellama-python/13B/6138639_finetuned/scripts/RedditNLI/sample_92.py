fine_premise = 14e9
fine_hypothesis = 14e9

# the hypothesis and premise mention the fine amount for Deutsche Bank
if fine_hypothesis!= fine_premise:
    # check if the fine amount in the hypothesis contradicts the fine amount in the premise
    label = "contradiction"
else:
    # if the fine amount in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
