fine_premise = 14
fine_hypothesis = 14

# the hypothesis and premise mention the fine amount related to Deutsche Bank
if fine_hypothesis!= fine_premise:
    # check if the fine amount in the hypothesis contradicts the fine amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
