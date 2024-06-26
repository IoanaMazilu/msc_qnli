# Define variables with representative names for the numerical entities in both inputs
jobs_premise = 36,000
rate_premise = 9.0%
jobs_hypothesis = 36,000
rate_hypothesis = 9%

# Extract all quantities as valid numbers (integers or floats)
jobs_premise = int(jobs_premise)
rate_premise = float(rate_premise)
jobs_hypothesis = int(jobs_hypothesis)
rate_hypothesis = float(rate_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if jobs_hypothesis!= jobs_premise:
    # Check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif rate_hypothesis < rate_premise:
    # Check if the unemployment rate in the hypothesis is less than the unemployment rate in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
