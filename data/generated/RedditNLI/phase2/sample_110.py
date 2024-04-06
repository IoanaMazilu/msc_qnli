# Premise: Pending sales of homes rose 1.5% in March, reversing February's decline.
# Hypothesis: Pending Sales of Existing Homes in U.S. Climbed 1.5% in March.
# Golden Label: entailment

sales_increase_premise = 1.5
sales_increase_hypothesis = 1.5

# the hypothesis and premise mention the percentage increase in pending home sales in March
if sales_increase_hypothesis != sales_increase_premise:
    # check if the percentage increase in the hypothesis contradicts the percentage increase in the premise
    label = "contradiction"
else:
    # if the sales increase percentage in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

