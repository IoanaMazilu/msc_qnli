# Define variables with representative names for the numerical entities in both inputs
leg_time_premise = 7
leg_time_hypothesis = 6

# Extract all quantities as valid numbers (integers or floats)
leg_time_premise = float(leg_time_premise)
leg_time_hypothesis = float(leg_time_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if leg_time_hypothesis <= leg_time_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'leg_time_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the time, any number of seconds greater than 'leg_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
