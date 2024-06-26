# Define variables with representative names for the numerical entities in both inputs
gdp_growth_premise = 0.045
gdp_growth_hypothesis = 0.045
new_jobs_premise = 2000000
new_jobs_hypothesis = 2000000

# Extract all quantities as valid numbers (integers or floats)
if gdp_growth_hypothesis!= gdp_growth_premise:
    # Check if the GDP growth in the hypothesis contradicts the GDP growth reported in the premise
    label = "contradiction"
elif new_jobs_hypothesis!= new_jobs_premise:
    # Check if the number of new jobs from the hypothesis contradicts the number of new jobs in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
