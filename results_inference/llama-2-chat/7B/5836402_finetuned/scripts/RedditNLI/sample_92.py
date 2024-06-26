fine_premise = 14e9
fine_hypothesis = 14e9

# the hypothesis and premise mention the fine imposed on Deutsche Bank
if fine_hypothesis!= fine_premise:
    # check if the fine in the hypothesis contradicts the fine in the premise
    label = "contradiction"
else:
    # if the fine values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
