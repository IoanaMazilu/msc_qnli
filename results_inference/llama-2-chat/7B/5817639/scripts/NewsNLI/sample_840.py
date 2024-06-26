# Define variables for premise and hypothesis
premise_bag = 1
hypothesis_bag = 2

# Extract quantities from premise and hypothesis
premise_iPads = float(premise_bag)
hypothesis_iPads = float(hypothesis_bag)

# Compare quantities
if premise_iPads!= hypothesis_iPads:
    # If the number of iPads in the hypothesis contradicts the number of iPads in the premise
    label = "contradiction"
else:
    # If the number of iPads in the hypothesis is the same as the number of iPads in the premise, we can infer entailment
    label = "entailment"

# Print the label
print(label)
