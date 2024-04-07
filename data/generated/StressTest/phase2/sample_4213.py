# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $4.00 per hour and a standard tip rate of less than 45% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $4.00 per hour and a standard tip rate of 15% of the cost of the orders she serves.
# Golden Label: neutral

hourly_wage_premise = 4.00
hourly_wage_hypothesis = 4.00
tip_rate_premise = 0.45
tip_rate_hypothesis = 0.15

# the hypothesis refers to the same hourly wage and tip rate as the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the mentioned hourly wage in the hypothesis contradicts the hourly wage mentioned in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the mentioned tip rate in the hypothesis contradicts the tip rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for the tip rate
    # any tip rate less than 'tip_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

