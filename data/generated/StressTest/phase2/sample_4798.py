# Premise: If she worked six more than 2-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked six 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: neutral

shifts_premise = 8
shifts_hypothesis = 8
rate_premise = 40
rate_hypothesis = 40

# the hypothesis refers to the number of shifts and the rate of Jill's orders per hour mentioned in the premise
if shifts_premise != shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
elif rate_premise != rate_hypothesis:
    # check if the rate of orders per hour in the hypothesis contradicts the rate of orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

