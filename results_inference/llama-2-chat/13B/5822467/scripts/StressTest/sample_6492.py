# Define variables with representative names for the numerical entities in both inputs
parents_amount_premise = 3 * 12  # 3% of the amount per month for 4 years
parents_amount_hypothesis = 7 * 12

# Extract all quantities as valid numbers (integers or floats)
parents_amount_premise = int(parents_amount_premise)
parents_amount_hypothesis = int(parents_amount_hypothesis)

# Perform calculations if necessary
four_years = 4 * 12
total_owed_premise = parents_amount_premise * four_years
total_owed_hypothesis = parents_amount_hypothesis * four_years

# Compare the variables
if parents_amount_hypothesis <= total_owed_premise:
    # Check if the hypothesis value contradicts the total owed in the premise
    label = "contradiction"
elif parents_amount_hypothesis > total_owed_premise:
    # Check if the hypothesis value entails the total owed in the premise
    label = "entailment"
else:
    # The hypothesis value is neutral with respect to the premise
    label = "neutral"

print(label)
