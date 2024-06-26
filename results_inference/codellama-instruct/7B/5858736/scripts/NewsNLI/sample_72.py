# Define variables with representative names for the numerical entities in both inputs
cholera_deaths_premise = 800
cholera_infected_premise = 16000

# Extract all quantities as valid numbers (integers or floats)
cholera_deaths_hypothesis = 800
cholera_infected_hypothesis = 16000

# Use brief comments to explain what comparison you do between the defined variables
if cholera_deaths_hypothesis!= cholera_deaths_premise:
    # Check if the number of cholera deaths in the hypothesis contradicts the number of cholera deaths in the premise
    label = "contradiction"
elif cholera_infected_hypothesis!= cholera_infected_premise:
    # Check if the number of cholera infected in the hypothesis contradicts the number of cholera infected in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
