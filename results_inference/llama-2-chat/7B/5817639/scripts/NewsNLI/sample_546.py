# Define variables for premise and hypothesis
premise_time = "Spanish GP"
hypothesis_time = "practice misdemeanor"

# Extract quantities from premise and hypothesis
premise_position = 5
hypothesis_position = 10

# Compare quantities
if premise_position!= hypothesis_position:
    # Contradiction
    label = "contradiction"
elif premise_time == hypothesis_time:
    # Entailment
    label = "entailment"
else:
    # Neutral
    label = "neutral"

print(label)
