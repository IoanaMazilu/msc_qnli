# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $4.00 per hour and a standard tip rate of less than 75% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $4.00 per hour and a standard tip rate of 15% of the cost of the orders she serves.
# Golden Label: neutral

hourly_wage_premise = 4.00
hourly_wage_hypothesis = 4.00
tip_rate_premise = 75
tip_rate_hypothesis = 15

# the hypothesis refers to Jill's hourly wage and tip rate, which are also mentioned in the premise
if hourly_wage_premise != hourly_wage_hypothesis:
    # check if the hypothesis hourly wage contradicts the premise hourly wage
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the hypothesis tip rate contradicts the premise tip rate
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

