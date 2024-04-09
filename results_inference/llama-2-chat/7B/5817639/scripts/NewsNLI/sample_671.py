# Define variables for premise and hypothesis
premise_inmates = 0
hypothesis_inmates = 200

# Extract numbers from premise and hypothesis
premise_inmates = float(premise_inmates)
hypothesis_inmates = float(hypothesis_inmates)

# Compare values
if hypothesis_inmates!= premise_inmates:
    # If the number of inmates in the hypothesis is different from the premise, check for contradiction
    label = "contradiction"
else:
    # If the values are the same, check for entailment
    label = "entailment"

# Print the label
print(label)
