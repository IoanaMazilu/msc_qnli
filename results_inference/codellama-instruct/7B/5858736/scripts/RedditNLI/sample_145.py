# Define variables with representative names for the numerical entities in both inputs
gdp_premise = 0
gdp_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
gdp_premise = float(gdp_premise)
gdp_hypothesis = float(gdp_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if gdp_hypothesis!= gdp_premise:
    # Check if the GDP in the hypothesis contradicts the GDP in the premise
    label = "contradiction"
else:
    # If the GDP values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
