# Premise: John's Bank's saving amount is decreased 20% due to loan payment and current balance is Rs.
# Hypothesis: John's Bank's saving amount is decreased 70% due to loan payment and current balance is Rs.
# Golden Label: contradiction

saving_decrease_premise = 20
saving_decrease_hypothesis = 70

# the hypothesis talks about the decrease in saving amount due to loan payment, which is also mentioned in the premise
if saving_decrease_hypothesis != saving_decrease_premise:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage mentioned in the premise
    label = "contradiction"
else:
    # if the decrease percentages are the same, we can infer entailment
    label = "entailment"

print(label)

