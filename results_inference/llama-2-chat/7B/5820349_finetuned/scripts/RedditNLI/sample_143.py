fine_premise = 1e9
fine_hypothesis = 1e9

# the hypothesis and premise mention the fine on Wells Fargo from the US
if fine_hypothesis!= fine_premise:
    # check if the fine in the hypothesis contradicts the fine in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
