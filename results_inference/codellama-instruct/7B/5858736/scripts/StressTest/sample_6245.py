# Define variables with representative names for the numerical entities in both inputs
preference_brand_a_premise = 60
total_population_premise = 120
total_population_hypothesis = 120

# Extract all quantities as valid numbers (integers or floats)
preference_brand_a_premise = float(preference_brand_a_premise)
total_population_premise = float(total_population_premise)
total_population_hypothesis = float(total_population_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if preference_brand_a_premise <= preference_brand_a_hypothesis:
    # Check if the estimate of 'preference_brand_a_hypothesis' contradicts the number of people who preferred Brand A in the premise
    label = "contradiction"
elif total_population_hypothesis!= total_population_premise:
    # Check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
