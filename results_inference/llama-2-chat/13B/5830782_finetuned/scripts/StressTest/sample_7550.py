decrease_percentage_premise = 30
decrease_percentage_hypothesis = 20

# the hypothesis talks about the decrease in the saving amount of John's bank, which is also mentioned in the premise
if decrease_percentage_hypothesis!= decrease_percentage_premise:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage reported in the premise
    label = "contradiction"
else:
    # if the decrease percentages are the same, we can infer entailment
    label = "entailment"

print(label)