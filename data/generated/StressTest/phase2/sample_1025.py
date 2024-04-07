# Premise: John's Bank's saving amount is decreased 50% due to loan payment and current balance is Rs.
# Hypothesis: John's Bank's saving amount is decreased less than 50% due to loan payment and current balance is Rs.
# Golden Label: contradiction

decrease_rate_premise = 50
decrease_rate_hypothesis = 50

# the hypothesis refers to the decrease rate of John's bank savings due to loan payment
if decrease_rate_hypothesis < decrease_rate_premise:
    # check if the decrease rate in the hypothesis contradicts the decrease rate reported in the premise
    label = "contradiction"
else:
    # if the decrease rate in the hypothesis is equal to the one in the premise, we can infer entailment
    label = "entailment"

print(label)

