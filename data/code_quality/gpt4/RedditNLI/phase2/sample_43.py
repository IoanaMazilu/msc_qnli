richest_percentage_premise = 0.001
richest_percentage_hypothesis = 0.001

# the hypothesis and premise mention the percentage of richest people paying income taxes
if richest_percentage_hypothesis != richest_percentage_premise:
    # check if the richest percentage in the hypothesis contradicts the richest percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
