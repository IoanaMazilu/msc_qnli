# Define variables for the numerical entities in both inputs
annual_borrowing_premise = 5000
annual_borrowing_hypothesis = 3000

# Extract all quantities as valid numbers
annual_borrowing_premise = float(annual_borrowing_premise)
annual_borrowing_hypothesis = float(annual_borrowing_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if annual_borrowing_hypothesis <= annual_borrowing_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'annual_borrowing_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the annual borrowing amount
    # Any number of pounds greater than 'annual_borrowing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
