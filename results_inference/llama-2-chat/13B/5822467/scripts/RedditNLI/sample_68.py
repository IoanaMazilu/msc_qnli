# Define variables with representative names for the numerical entities in both inputs
jobs_premise = 321000
unemployment_premise = 5.8

# Extract all quantities as valid numbers (integers or floats)
jobs_hypothesis = int(321000)
unemployment_hypothesis = float(5.8)

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Compare the number of jobs in the premise and hypothesis
if jobs_premise!= jobs_hypothesis:
    # Check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif jobs_hypothesis < min_jobs_premise:
    # Check if the estimated number of jobs in the hypothesis contradicts the premise estimate of more than 'jobs_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of jobs
    # Any estimate of the number of jobs in the hypothesis greater or equal to 'jobs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# Compare the unemployment rate in the premise and hypothesis
if unemployment_premise!= unemployment_hypothesis:
    # Check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
elif unemployment_hypothesis > max_unemployment_premise:
    # Check if the estimated unemployment rate in the hypothesis contradicts the premise estimate of less than or equal to 'unemployment_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the unemployment rate
    # Any estimate of the unemployment rate in the hypothesis less or equal to 'unemployment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
