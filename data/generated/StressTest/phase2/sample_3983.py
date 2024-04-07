# Premise: Adams's internet provider offers unlimited traffic which costs $0.5 per day charged off at 12 a.
# Hypothesis: Adams's internet provider offers unlimited traffic which costs $0.5 per day charged off at more than 12 a.
# Golden Label: contradiction

charge_time_premise = 12
charge_cost_premise = 0.5
charge_time_hypothesis = 12
charge_cost_hypothesis = 0.5

# the hypothesis refers to the charge time and cost mentioned in the premise
if charge_time_premise >= charge_time_hypothesis:
    # check if the hypothesis estimate contradicts the charge time in the premise
    label = "contradiction"
elif charge_cost_hypothesis != charge_cost_premise:
    # check if the cost in the hypothesis contradicts the cost reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

