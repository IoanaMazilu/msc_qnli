# Premise: David's Bank's saving amount is decreased 10% due to loan payment and current balance is Rs.
# Hypothesis: David's Bank's saving amount is decreased 40% due to loan payment and current balance is Rs.
# Golden Label: contradiction

decrease_premise = 10
decrease_hypothesis = 40

# the hypothesis talks about the percentage decrease in savings due to loan payment, which is also mentioned in the premise
if decrease_premise != decrease_hypothesis:
    # check if the percentage decrease in the hypothesis contradicts the percentage decrease reported in the premise
    label = "contradiction"
else:
    # if the decrease percentages do not contradict, we can infer entailment
    label = "entailment"

print(label)

