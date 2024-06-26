# Define variables for the premise and hypothesis
premise_rainfall = 25
hypothesis_rainfall = 25

# Check if the hypothesis value contradicts the premise
if hypothesis_rainfall <= premise_rainfall:
    label = "contradiction"
else:
    # The hypothesis value is greater than the premise, so the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
