# Define variables with representative names for the numerical entities in both inputs
annual_borrowing_premise = 6500
annual_borrowing_hypothesis = 1500

# Extract all quantities as valid numbers (integers or floats)

# Check if the hypothesis value contradicts the estimate of more than 'annual_borrowing_premise'
if annual_borrowing_hypothesis <= annual_borrowing_premise:
    label = "contradiction"
else:
    # Any number of pounds greater than 'annual_borrowing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
