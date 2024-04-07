# Premise: If she worked four more than 7-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four 9-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: neutral

shifts_premise = 7 + 4
shifts_hypothesis = 9 * 4
orders_per_hour = 40

# the hypothesis refers to the number of worked hours and the average orders per hour mentioned in the premise
# we calculate the total earnings for both premise and hypothesis
total_earning_premise = shifts_premise * orders_per_hour
total_earning_hypothesis = shifts_hypothesis * orders_per_hour

if total_earning_premise != total_earning_hypothesis:
    # check if the total earnings in the hypothesis contradicts the total earnings in the premise
    label = "contradiction"
else:
    # if the total earnings in the hypothesis does not contradict the total earnings in the premise, we can infer entailment
    label = "entailment"

print(label)

