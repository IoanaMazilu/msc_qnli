fine_premise = 14
fine_hypothesis = 14

# the hypothesis and premise mention a fine of $14 billion awarded to Deutsche Bank
if fine_hypothesis!= fine_premise:
    # check if the fine amount in the hypothesis contradicts the fine amount in the premise
    label = "contradiction"
else:
    # if the fine amount in the hypothesis does not contradict the fine amount in the premise, we can infer entailment
    label = "entailment"

print(label)
