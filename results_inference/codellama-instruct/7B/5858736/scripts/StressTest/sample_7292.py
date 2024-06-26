# Define variables for the numerical entities in the premise and hypothesis
premise_amount = 600
premise_share = "Rs."
hypothesis_amount = 400
hypothesis_share = "Rs."

# Extract all quantities as valid numbers
premise_amount = float(premise_amount)
hypothesis_amount = float(hypothesis_amount)

# Use brief comments to explain what comparison you do between the defined variables
if premise_amount <= hypothesis_amount:
    # Check if the hypothesis value contradicts the premise amount
    label = "contradiction"
elif premise_share!= hypothesis_share:
    # Check if the premise share type contradicts the hypothesis share type
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
