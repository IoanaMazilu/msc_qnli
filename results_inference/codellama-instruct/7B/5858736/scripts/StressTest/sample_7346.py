premise_crude_price = 28
hypothesis_crude_price = 28

# the hypothesis refers to the number of sold cookies and pies mentioned in the premise
if premise_crude_price <= hypothesis_crude_price:
    # check if the estimate of 'hypothesis_crude_price' contradicts the number of cookie sales in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
