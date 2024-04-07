# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $8.00 per hour and a standard tip rate of 30% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $8.00 per hour and a standard tip rate of less than 30% of the cost of the orders she serves.
# Golden Label: contradiction

hourly_wage_premise = 8.00
hourly_wage_hypothesis = 8.00
tip_rate_premise = 30
tip_rate_hypothesis = 30

# The hypothesis refers to the hourly wage and tip rate mentioned in the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

