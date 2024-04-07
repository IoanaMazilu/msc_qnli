# Premise: 3450 from Anwar at 6% p.
# Hypothesis: 5450 from Anwar at 6% p.
# Golden Label: contradiction

amount_premise = 3450
amount_hypothesis = 5450

# the hypothesis refers to a loan amount from Anwar mentioned in the premise
if amount_hypothesis == amount_premise:
    # check if the loan amount in the hypothesis matches the loan amount reported in the premise
    label = "entailment"
elif amount_hypothesis < amount_premise:
    # check if the loan amount in the hypothesis contradicts the loan amount reported in the premise
    label = "contradiction"
else:
    # if the loan amount in the hypothesis is greater than the loan amount in the premise, this doesn't contradict the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)

