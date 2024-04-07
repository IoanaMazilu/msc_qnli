# Premise: Carol budgeted 18 dollars for gifts for each of the 15 people on her Christmas list.
# Hypothesis: Carol budgeted 68 dollars for gifts for each of the 15 people on her Christmas list.
# Golden Label: contradiction

gift_budget_premise = 18
gift_budget_hypothesis = 68
people_premise = 15
people_hypothesis = 15

# the hypothesis refers to the budget for gifts and number of people mentioned in the premise
if gift_budget_hypothesis != gift_budget_premise:
    # check if the budget for gifts in the hypothesis contradicts the budget for gifts reported in the premise
    label = "contradiction"
elif people_hypothesis != people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

