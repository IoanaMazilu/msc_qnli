# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $5.00 per hour and a standard tip rate of 25% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $5.00 per hour and a standard tip rate of less than 65% of the cost of the orders she serves.
# Golden Label: entailment

hourly_wage_premise = 5.00
hourly_wage_hypothesis = 5.00
tip_rate_premise = 25
tip_rate_hypothesis = 65

# the hypothesis refers to the hourly wage and tip rate which are also mentioned in the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis <= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # the premise gives specific values for the hourly wage and tip rate
    # the hourly wage in the hypothesis matches the premise
    # the tip rate in the hypothesis is greater than the premise, which does not contradict the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)

