# Define variables for the numerical entities in the premise and hypothesis
payroll_jobs_premise = 144,000
unemployment_rate_premise = 5.4
unemployment_rate_premise_previous = 5.5
jobless_rate_premise = 5.5

# Define variables for the numerical entities in the hypothesis
new_jobs_hypothesis = nearly 1 of every 5 of the new jobs created during the last 12 months

# Extract all quantities as valid numbers (integers or floats)
payroll_jobs_premise = int(payroll_jobs_premise.replace(",", ""))
unemployment_rate_premise = float(unemployment_rate_premise)
unemployment_rate_premise_previous = float(unemployment_rate_premise_previous)
jobless_rate_premise = float(jobless_rate_premise)

# Use brief comments to explain what comparison you do between the defined variables
if payroll_jobs_premise!= new_jobs_hypothesis:
    # check if the number of payroll jobs in the premise contradicts the number of new jobs in the hypothesis
    label = "contradiction"
elif unemployment_rate_premise!= unemployment_rate_premise_previous:
    # check if the unemployment rate in the premise contradicts the unemployment rate in the previous month
    label = "contradiction"
elif jobless_rate_premise!= unemployment_rate_premise:
    # check if the jobless rate in the premise contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
