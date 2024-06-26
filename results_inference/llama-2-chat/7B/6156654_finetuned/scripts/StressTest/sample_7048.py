# Define the premise and hypothesis
premise = 62
hypothesis = 12

# The hypothesis talks about the percentage below cost price, which is also mentioned in the premise
if hypothesis >= premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif hypothesis < premise:
    # If the hypothesis value is less than the premise value, it is a confirmation
    label = "entailment"
else:
    # If the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
