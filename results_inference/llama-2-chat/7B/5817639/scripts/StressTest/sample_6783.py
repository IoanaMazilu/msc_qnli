# Define variables for the numerical entities in the premise and hypothesis
hourly_wage_premise = float(input("Enter the hourly wage for the first 40 hours: "))
hourly_wage_hypothesis = float(input("Enter the hourly wage for the first less than 70 hours: "))
total_hours_premise = int(input("Enter the total number of hours worked in a week: "))
total_hours_hypothesis = int(input("Enter the total number of hours worked in a week: "))

# Compare the variables to determine the relation between the premise and hypothesis
if total_hours_hypothesis <= total_hours_premise:
    # Check if the hypothesis value contradicts the estimate of total hours in the premise
    label = "contradiction"
elif hourly_wage_hypothesis!= hourly_wage_premise:
    # Check if the hypothesis value contradicts the estimate of hourly wage in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
