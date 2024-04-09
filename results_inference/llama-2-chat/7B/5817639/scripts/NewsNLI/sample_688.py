# Define variables for premise and hypothesis
premise = 3
hypothesis = 3

# Extract quantities from the premise and hypothesis
premise_quantity = int(premise)
hypothesis_quantity = int(hypothesis)

# Compare the quantities
if premise_quantity!= hypothesis_quantity:
    # If the quantities are different, check if the hypothesis contradicts the premise
    if hypothesis_quantity < premise_quantity:
        # If the hypothesis quantity is less than the premise quantity, label the inference as contradiction
        label = "contradiction"
    else:
        # If the hypothesis quantity is greater than or equal to the premise quantity, label the inference as neutral
        label = "neutral"
else:
    # If the quantities are the same, label the inference as entailment
    label = "entailment"

print(label)
