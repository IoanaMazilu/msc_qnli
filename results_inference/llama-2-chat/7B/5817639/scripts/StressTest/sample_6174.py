# Define variables for premise and hypothesis
commute_time_premise = 15
commute_time_hypothesis = 55

# Check if the hypothesis value contradicts the estimate in the premise
if commute_time_hypothesis <= commute_time_premise:
    label = "contradiction"
else:
    # The premise only gives an estimate, so the hypothesis value cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
