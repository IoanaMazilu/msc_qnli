# Define variables with representative names for the numerical entities in both inputs
age_amar = 35
age_akbar = 40
age_anthony = 21
total_ages = 86

# Extract all quantities as valid numbers (integers or floats)
total_ages = 86

# Use brief comments to explain what comparison you do between the defined variables
if total_ages <= (age_amar + age_akbar + age_anthony):
    # Check if the hypothesis value contradicts the estimate of less than 'total_ages'
    label = "contradiction"
else:
    # The premise gives only an estimate for the total of the ages
    # Any number of ages greater than 'total_ages' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
