# Premise: Loblaw expects higher minimum wage rules will increase its labour costs by $190M.
# Hypothesis: Loblaw says minimum wage increases will hike labour costs by $190M.
# Golden Label: entailment

labour_costs_increase_premise = 190
labour_costs_increase_hypothesis = 190

# the hypothesis and premise mention the estimated increase in labour costs due to higher minimum wage rules
if labour_costs_increase_hypothesis != labour_costs_increase_premise:
    # check if the estimated increase in labour costs in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

