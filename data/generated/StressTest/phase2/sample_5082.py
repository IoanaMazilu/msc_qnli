# Premise: Jill works as a waitress at the local diner where she earns an hourly wage of $7.00 per hour and a standard tip rate of 5% of the cost of the orders she serves.
# Hypothesis: Jill works as a waitress at the local diner where she earns an hourly wage of $7.00 per hour and a standard tip rate of less than 6% of the cost of the orders she serves.
# Golden Label: entailment

hourly_wage_premise = 7.00
hourly_wage_hypothesis = 7.00
tip_rate_premise = 5
tip_rate_hypothesis = 6

# the hypothesis refers to the hourly wage and tip rate of Jill mentioned in the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis <= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

