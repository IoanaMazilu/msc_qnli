# Define variables for the numerical entities in the premise and hypothesis
purchase_price_premise = 20
purchase_quantity_premise = 60
purchase_from_premise = "Ram"
purchase_to_premise = "Mohan"

purchase_price_hypothesis = 20
purchase_quantity_hypothesis = 60
purchase_from_hypothesis = "Ram"
purchase_to_hypothesis = "Mohan"

# Extract all quantities as valid numbers
purchase_price_premise = float(purchase_price_premise)
purchase_quantity_premise = float(purchase_quantity_premise)
purchase_price_hypothesis = float(purchase_price_hypothesis)
purchase_quantity_hypothesis = float(purchase_quantity_hypothesis)

# Check if the hypothesis values and estimates do not contradict the premise ones
if purchase_price_hypothesis <= purchase_price_premise and purchase_quantity_hypothesis <= purchase_quantity_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
