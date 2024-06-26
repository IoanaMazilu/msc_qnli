# Define variables with representative names for the numerical entities in both inputs
num_hours_premise = 10
num_hours_hypothesis = 70

# Extract all quantities as valid numbers (integers or floats)
num_hours_premise = int(num_hours_premise)
num_hours_hypothesis = int(num_hours_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if num_hours_hypothesis <= num_hours_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'num_hours_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of hours, any number of hours greater than 'num_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
