# Define variables with representative names for the numerical entities in both inputs
gdp_growth_premise = 2.2
gdp_growth_hypothesis = 2.2

# Extract all quantities as valid numbers (integers or floats)
gdp_growth_premise = float(gdp_growth_premise)
gdp_growth_hypothesis = float(gdp_growth_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if gdp_growth_hypothesis!= gdp_growth_premise:
    # Check if the estimated GDP growth rate in the hypothesis contradicts the premise estimate of 2.2%
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
