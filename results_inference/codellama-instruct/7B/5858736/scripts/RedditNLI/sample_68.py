# Extract numerical information from the premise
number_jobs = 321000
unemployment_rate = 5.8

# Extract numerical information from the hypothesis
number_jobs_hypothesis = 321000
unemployment_rate_hypothesis = 5.8

# Compare the numerical information
if number_jobs!= number_jobs_hypothesis:
    # Check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif unemployment_rate!= unemployment_rate_hypothesis:
    # Check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
