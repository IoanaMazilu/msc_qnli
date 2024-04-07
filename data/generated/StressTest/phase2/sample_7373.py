# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $10.00 per hour and a standard tip rate of 40% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $10.00 per hour and a standard tip rate of more than 40% of the cost of the orders she serves.
# Golden Label: contradiction

hourly_wage_premise = 10.00
hourly_wage_hypothesis = 10.00
tip_rate_premise = 40
tip_rate_hypothesis = 40

# the hypothesis refers to the wage and tip rate of Jill mentioned in the premise
if hourly_wage_premise != hourly_wage_hypothesis:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_premise >= tip_rate_hypothesis:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact tip rate, any tip rate greater than 'tip_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

