# Define variables for the numerical entities in the input
premise_time = 120
hypothesis_time = 520

# Compare the values of the variables
if hypothesis_time <= premise_time:
    # Check if the hypothesis time contradicts the premise time
    label = "contradiction"
elif hypothesis_time > premise_time:
    # Check if the hypothesis time entails the premise time
    label = "entailment"
else:
    # If the hypothesis time is neutral with respect to the premise time, no comparison is needed
    label = "neutral"

print(label)
