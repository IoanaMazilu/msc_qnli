premise_crude_price = 28
hypothesis_crude_price = 68

if premise_crude_price <= hypothesis_crude_price:
    label = "contradiction"
else:
    label = "entailment"

print(label)
