# Define variables for the premise and hypothesis
premise_amount = 14.3e9  # 14.3 billion euros
hypothesis_cost = 14.3e9  # 14.3 billion euros

# Check if the hypothesis value contradicts the premise value
if hypothesis_cost!= premise_amount:
    # If the values do not match, label the comparison as contradiction
    label = "contradiction"
elif hypothesis_cost > premise_amount:
    # If the hypothesis value is greater than the premise value, label the comparison as entailment
    label = "entailment"
else:
    # If the hypothesis value is equal to the premise value, label the comparison as neutral
    label = "neutral"

print(label)
