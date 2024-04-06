# Premise: Loblaw says minimum wage increases will hike labour costs by $190M.
# Hypothesis: Loblaw expects higher minimum wage rules will increase its labour costs by $190M.
# Golden Label: entailment

cost_increase_premise = 190
cost_increase_hypothesis = 190

# the hypothesis and premise mention the increase in labour costs for Loblaw due to minimum wage increases
if cost_increase_hypothesis != cost_increase_premise:
    # check if the cost increase in the hypothesis contradicts the cost increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
