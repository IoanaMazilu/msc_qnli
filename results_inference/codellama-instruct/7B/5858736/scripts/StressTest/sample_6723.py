# Define variables with representative names for the numerical entities in both inputs
premise_amount = 3600
premise_percentage = 6
hypothesis_amount = 1600
hypothesis_percentage = 6

# Extract all quantities as valid numbers (integers or floats)
premise_amount = int(premise_amount)
premise_percentage = float(premise_percentage)
hypothesis_amount = int(hypothesis_amount)
hypothesis_percentage = float(hypothesis_percentage)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_amount <= premise_amount:
    # Check if the hypothesis value contradicts the premise amount
    label = "contradiction"
elif hypothesis_percentage!= premise_percentage:
    # Check if the hypothesis percentage contradicts the premise percentage
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
