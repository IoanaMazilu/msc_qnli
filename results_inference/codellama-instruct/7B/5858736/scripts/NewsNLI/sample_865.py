# Define variables for the numerical entities in the premise and hypothesis
num_dead_premise = 2
num_injured_premise = 2

num_injured_hypothesis = 25

# Extract all quantities as valid numbers
gdp_growth_premise = float(gdp_growth_premise)
gdp_growth_hypothesis = float(gdp_growth_hypothesis)
new_jobs_premise = int(new_jobs_premise)
new_jobs_hypothesis = int(new_jobs_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if num_injured_hypothesis > num_injured_premise:
    # Check if the number of injured students in the hypothesis exceeds the number of injured students in the premise
    label = "entailment"
else:
    # If the number of injured students in the hypothesis does not exceed the number of injured students in the premise, we can infer neutrality
    label = "neutral"

print(label)
