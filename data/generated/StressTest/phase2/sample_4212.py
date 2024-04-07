# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $4.00 per hour and a standard tip rate of 15% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $4.00 per hour and a standard tip rate of less than 45% of the cost of the orders she serves.
# Golden Label: entailment

hourly_wage_premise = 4.00
hourly_wage_hypothesis = 4.00
tip_rate_premise = 0.15
tip_rate_hypothesis = 0.45

# the hypothesis refers to the same waitress, hourly wage and tip rate mentioned in the premise
if hourly_wage_premise != hourly_wage_hypothesis:
    # check if the hourly wage in the hypothesis contradicts the hourly wage mentioned in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

