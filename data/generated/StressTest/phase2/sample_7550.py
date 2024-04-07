# Premise: John's Bank's saving amount is decreased 30% due to loan payment and current balance is Rs.
# Hypothesis: John's Bank's saving amount is decreased 20% due to loan payment and current balance is Rs.
# Golden Label: contradiction

saving_decrease_premise = 30
saving_decrease_hypothesis = 20

# the hypothesis refers to the same percentage decrease in saving amount as in the premise
if saving_decrease_premise != saving_decrease_hypothesis:
    # check if the percentage decrease in the hypothesis contradicts the percentage decrease in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

