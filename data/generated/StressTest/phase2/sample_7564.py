# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $8.00 per hour and a standard tip rate of less than 70% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $8.00 per hour and a standard tip rate of 30% of the cost of the orders she serves.
# Golden Label: neutral

hourly_wage_premise = 8.00
hourly_wage_hypothesis = 8.00
tip_rate_premise = 70
tip_rate_hypothesis = 30

# the hypothesis talks about Jill's hourly wage and the tip rate, both mentioned in the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the estimate of less than 'tip_rate_premise'
    label = "contradiction"
else:
    # both the hourly wage and the tip rate in the hypothesis are consistent with the premise
    # but the exact tip rate cannot be explicitly entailed from the premise, as it only provides an upper limit
    label = "neutral"

print(label)

