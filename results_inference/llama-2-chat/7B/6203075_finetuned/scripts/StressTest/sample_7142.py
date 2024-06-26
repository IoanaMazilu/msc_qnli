# Define the premise and hypothesis as dictionaries
premise = {"departure_rate": 50}
hypothesis = {"departure_rate": 10}

# Define the variables for the comparison
departure_rate_premise = 50
departure_rate_hypothesis = 10

# The hypothesis talks about the departure rate of the next three flights,
# which is also referenced in the premise
if departure_rate_hypothesis >= departure_rate_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # Check if the hypothesis value is less than the premise value
    # This is consistent with the premise, so we can infer entailment
    label = "entailment"
else:
    # If the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
