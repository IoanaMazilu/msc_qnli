# Premise: 55000 respectively, after three months Mitra invested Rs.
# Hypothesis: 75000 respectively, after three months Mitra invested Rs.
# Golden Label: contradiction

investment_premise = 55000
investment_hypothesis = 75000

# the hypothesis refers to the amount invested by Mitra mentioned in the premise
if investment_hypothesis != investment_premise:
    # check if the amount in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis amount does not contradict the premise amount, we can infer entailment
    label = "entailment"

print(label)

