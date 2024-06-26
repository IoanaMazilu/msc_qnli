saving_decrease_premise = 10
saving_decrease_hypothesis = 40

# the hypothesis refers to the decrease in saving amount due to loan payment mentioned in the premise
if saving_decrease_premise!= saving_decrease_hypothesis:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage reported in the premise
    label = "contradiction"
else:
    # if the decrease percentages in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
