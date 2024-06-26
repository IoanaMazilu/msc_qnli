shirts_bought_premise = 160
shirts_bought_hypothesis = 660

# the hypothesis refers to the number of shirts bought, which is also mentioned in the premise
if shirts_bought_hypothesis != shirts_bought_premise:
    # check if the number of shirts bought in the hypothesis contradicts the number of shirts bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)