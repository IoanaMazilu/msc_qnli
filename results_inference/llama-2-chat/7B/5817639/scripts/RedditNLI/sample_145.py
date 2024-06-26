# Define variables for the premise and hypothesis
premise_gdp_growth = 0.5
hypothesis_gdp_growth = 0.7

# Check if the hypothesis growth rate contradicts the premise growth rate
if hypothesis_gdp_growth < premise_gdp_growth:
    label = "contradiction"
elif hypothesis_gdp_growth > premise_gdp_growth:
    label = "entailment"
else:
    label = "neutral"

print(label)
