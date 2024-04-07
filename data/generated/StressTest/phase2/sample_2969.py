# Premise: Find the annual dividend of Sam owing 2000 shares of the company having a par value of Rs.
# Hypothesis: Find the annual dividend of Sam owing 1000 shares of the company having a par value of Rs.
# Golden Label: contradiction

shares_premise = 2000
shares_hypothesis = 1000

# the hypothesis refers to the number of shares owned by Sam as mentioned in the premise
if shares_hypothesis != shares_premise:
    # check if the number of shares in the hypothesis contradicts the number of shares reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

