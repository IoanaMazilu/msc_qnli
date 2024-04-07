# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $4.00 per hour and a standard tip rate of 15% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $4.00 per hour and a standard tip rate of 65% of the cost of the orders she serves.
# Golden Label: contradiction

hourly_wage_premise = 4.00
hourly_wage_hypothesis = 4.00
tip_rate_premise = 15
tip_rate_hypothesis = 65

# the hypothesis refers to the hourly wage and the standard tip rate of Jill which is also mentioned in the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage mentioned in the premise
    label = "contradiction"
elif tip_rate_hypothesis != tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate mentioned in the premise
    label = "contradiction"
else:
    # if the wage and tip rate in the hypothesis do not contradict the premise ones, they are exactly the same, so we can infer entailment
    label = "entailment"

print(label)

