# Define variables with representative names for the numerical entities in both inputs
job_time_premise = 85
job_time_hypothesis = 15

# Extract all quantities as valid numbers (integers or floats)
job_time_premise = float(job_time_premise)
job_time_hypothesis = float(job_time_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if job_time_hypothesis <= job_time_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'job_time_premise'
    label = "contradiction"
else:
    # The hypothesis value is greater than the estimate of less than 'job_time_premise', so the hypothesis is entailed from the premise
    label = "entailment"

print(label)
