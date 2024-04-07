# Premise: Lally's internet provider offers unlimited traffic which costs $0.5 per day charged off at less than 52 a.
# Hypothesis: Lally's internet provider offers unlimited traffic which costs $0.5 per day charged off at 12 a.
# Golden Label: neutral

cost_per_day_premise = 0.5
cost_per_day_hypothesis = 0.5
annual_charge_premise = 52
annual_charge_hypothesis = 12

# the hypothesis refers to the cost per day and the annual charge for the internet service mentioned in the premise
if cost_per_day_premise != cost_per_day_hypothesis:
    # check if the cost per day in the hypothesis contradicts the cost per day reported in the premise
    label = "contradiction"
elif annual_charge_hypothesis >= annual_charge_premise:
    # check if the hypothesis value contradicts the estimate of less than 'annual_charge_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

