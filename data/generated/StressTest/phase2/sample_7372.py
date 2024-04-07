# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $10.00 per hour and a standard tip rate of less than 80% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $10.00 per hour and a standard tip rate of 40% of the cost of the orders she serves.
# Golden Label: neutral

wage_hour_premise = 10.00
wage_hour_hypothesis = 10.00
tip_rate_premise = 80
tip_rate_hypothesis = 40

# the hypothesis refers to the wages and tips of a waitress mentioned in the premise
if wage_hour_hypothesis != wage_hour_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the premise's estimate of 'less than tip_rate_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
