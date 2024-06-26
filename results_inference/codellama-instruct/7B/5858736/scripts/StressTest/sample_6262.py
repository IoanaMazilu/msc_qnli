# Define variables with representative names for the numerical entities in both inputs
annie_working_alone_premise = 40
annie_working_alone_hypothesis = 10

# Extract all quantities as valid numbers (integers or floats)
annie_working_alone_premise = float(annie_working_alone_premise)
annie_working_alone_hypothesis = float(annie_working_alone_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if annie_working_alone_hypothesis <= annie_working_alone_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'annie_working_alone_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of hours
    # Any number of hours greater than 'annie_working_alone_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
