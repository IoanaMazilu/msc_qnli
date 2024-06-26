# Define variables with representative names for the numerical entities in both inputs
premise_amount = 3600
premise_interest_rate = 6
hypothesis_amount = 3600
hypothesis_interest_rate = 6

# Extract all quantities as valid numbers (integers or floats)
premise_amount = float(premise_amount)
premise_interest_rate = float(premise_interest_rate)
hypothesis_amount = float(hypothesis_amount)
hypothesis_interest_rate = float(hypothesis_interest_rate)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_amount <= premise_amount:
    # Check if the hypothesis value contradicts the amount mentioned in the premise
    label = "contradiction"
elif hypothesis_interest_rate!= premise_interest_rate:
    # Check if the interest rate in the hypothesis contradicts the interest rate mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
