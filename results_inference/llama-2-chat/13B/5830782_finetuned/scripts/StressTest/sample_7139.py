saving_decrease_premise = 10
saving_decrease_hypothesis = 40

# the hypothesis talks about the decrease in savings mentioned in the premise
if saving_decrease_hypothesis!= saving_decrease_premise:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage reported in the premise
    label = "contradiction"
else:
    # if the decrease percentages are the same, we can infer entailment
    label = "entailment"

print(label)
