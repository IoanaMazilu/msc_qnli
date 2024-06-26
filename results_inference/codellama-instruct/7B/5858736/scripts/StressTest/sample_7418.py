# Define variables with representative names for the numerical entities in both inputs
age_molly_now = 18
age_molly_six_years_ago = 6

# Extract all quantities as valid numbers (integers or floats)
age_molly_now = int(age_molly_now)
age_molly_six_years_ago = int(age_molly_six_years_ago)

# Use brief comments to explain what comparison you do between the defined variables
if age_molly_now * 5 <= age_molly_six_years_ago:
    # Check if the estimate of 'age_molly_now * 5' contradicts the number of years since Molly's age six years ago
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
