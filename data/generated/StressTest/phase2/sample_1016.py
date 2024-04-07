# Premise: John's Bank's saving amount is decreased 12% due to loan payment and current balance is Rs.
# Hypothesis: John's Bank's saving amount is decreased 32% due to loan payment and current balance is Rs.
# Golden Label: contradiction

decrease_percentage_premise = 12
decrease_percentage_hypothesis = 32

# the hypothesis refers to the percentage decrease of John's bank savings, which is also mentioned in the premise
if decrease_percentage_hypothesis != decrease_percentage_premise:
    # check if the percentage decrease in the hypothesis contradicts the percentage decrease reported in the premise
    label = "contradiction"
else:
    # if the percentage decrease in the hypothesis and premise is same, we can infer entailment
    label = "entailment"

print(label)

