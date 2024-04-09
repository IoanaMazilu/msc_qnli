# Define variables with representative names for the numerical entities in both inputs
tax_premise = 20
rebate_premise = 10
item_price_premise = 90

# Extract all quantities as valid numbers (integers or floats)
tax_hypothesis = float(input("Enter the sales tax rate: "))
rebate_hypothesis = float(input("Enter the rebate amount after tax: "))
item_price_hypothesis = float(input("Enter the item price: "))

# Perform calculations if necessary
total_cost_premise = tax_premise + item_price_premise
total_cost_hypothesis = tax_hypothesis + item_price_hypothesis

# Compare the variables and determine the label
if item_price_hypothesis <= item_price_premise:
    # Check if the estimate of 'item_price_hypothesis' contradicts the item price in the premise
    label = "contradiction"
elif tax_hypothesis!= tax_premise or rebate_hypothesis!= rebate_premise:
    # Check if the tax or rebate amounts in the hypothesis contradict the amounts in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
