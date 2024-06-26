# Define variables with representative names for the numerical entities in both inputs
cleaning_time_premise = 1
cleaning_time_hypothesis = 6

# Extract all quantities as valid numbers (integers or floats)
cleaning_time_premise = float(cleaning_time_premise)
cleaning_time_hypothesis = float(cleaning_time_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if cleaning_time_hypothesis <= cleaning_time_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'cleaning_time_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the cleaning time
    # Any number of hours greater than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
