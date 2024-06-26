purchase_quantity_premise = 12
purchase_quantity_hypothesis = 12
purchase_price_premise = 42.00
purchase_price_hypothesis = 42.00

# the hypothesis refers to the same purchase quantity and price as the premise
if purchase_quantity_hypothesis <= purchase_quantity_premise:
    label = "contradiction"
elif purchase_price_hypothesis!= purchase_price_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
