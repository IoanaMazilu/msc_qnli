hourly_wage_premise = 20
additional_hourly_wage_premise = 2
hours_worked_premise = 40

# define variables for the hypothesis
hourly_wage_hypothesis = float(input("Enter the hourly wage for more than 40 hours: "))
additional_hourly_wage_hypothesis = float(input("Enter the additional hourly wage for each additional hour worked: "))
hours_worked_hypothesis = float(input("Enter the number of hours worked: "))

# compare the values of the premise and hypothesis
if hours_worked_hypothesis > hours_worked_premise:
    # the hypothesis refers to a higher number of hours worked than the premise
    label = "entailment"
elif hours_worked_hypothesis <= hours_worked_premise:
    # the hypothesis refers to the same or fewer hours worked as the premise
    label = "neutral"
else:
    # the hypothesis contradicts the premise, as it refers to more hours worked than the premise
    label = "contradiction"

# perform calculations to compare the hourly wages
hourly_wage_diff = hourly_wage_hypothesis - hourly_wage_premise
additional_hourly_wage_diff = additional_hourly_wage_hypothesis - additional_hourly_wage_premise

# check if the hypothesis values contradict the premise values
if hourly_wage_diff < 0 or additional_hourly_wage_diff < 0:
    label = "contradiction"

print(label)
