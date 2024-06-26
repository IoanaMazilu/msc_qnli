# Define variables for the numerical entities in the premise and hypothesis
premise_cases = 49
hypothesis_cases = 24

# Extract all quantities as valid numbers
premise_cases = int(premise_cases)
hypothesis_cases = int(hypothesis_cases)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_cases > premise_cases:
    # Check if the number of cases in the hypothesis exceeds the number of cases in the premise
    label = "entailment"
else:
    # If the number of cases in the hypothesis does not exceed the number of cases in the premise, we can infer neutrality
    label = "neutral"

print(label)
