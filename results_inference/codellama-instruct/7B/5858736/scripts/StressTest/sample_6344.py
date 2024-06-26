# Define variables for the numerical entities in the premise and hypothesis
premise_amount = 288
premise_discount = 10
hypothesis_amount = 888
hypothesis_discount = 10

# Extract all quantities as valid numbers
premise_amount = int(premise_amount)
premise_discount = int(premise_discount)
hypothesis_amount = int(hypothesis_amount)
hypothesis_discount = int(hypothesis_discount)

# Use brief comments to explain what comparison you do between the defined variables
if premise_amount <= hypothesis_amount:
    # Check if the estimate of 'hypothesis_amount' contradicts the amount mentioned in the premise
    label = "contradiction"
elif premise_discount <= hypothesis_discount:
    # Check if the estimate of 'hypothesis_discount' contradicts the discount mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
