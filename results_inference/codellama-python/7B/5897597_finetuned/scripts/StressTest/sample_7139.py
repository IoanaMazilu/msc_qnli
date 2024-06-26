decrease_percentage_premise = 10
decrease_percentage_hypothesis = 40

# the hypothesis refers to the decrease percentage of the saving amount in David's Bank, mentioned in the premise
if decrease_percentage_hypothesis!= decrease_percentage_premise:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage reported in the premise
    label = "contradiction"
else:
    # if the decrease percentages in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
