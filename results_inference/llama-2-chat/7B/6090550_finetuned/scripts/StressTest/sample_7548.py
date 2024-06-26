saving_decrease_premise = 30
saving_decrease_hypothesis = 80

# the hypothesis talks about the decrease in the saving amount, which is also mentioned in the premise
if saving_decrease_hypothesis <= saving_decrease_premise:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage in the premise
    label = "contradiction"
else:
    # if the decrease percentage in the hypothesis is greater than the decrease percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

