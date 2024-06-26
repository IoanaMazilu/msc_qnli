# Define variables with representative names for the numerical entities in both inputs
job_time_premise = 15
job_time_hypothesis = 15

# Extract all quantities as valid numbers (integers or floats)
job_time_premise = int(job_time_premise)
job_time_hypothesis = int(job_time_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if job_time_hypothesis <= job_time_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'job_time_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the time it takes to do a job alone
    # Any number of hours greater than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
