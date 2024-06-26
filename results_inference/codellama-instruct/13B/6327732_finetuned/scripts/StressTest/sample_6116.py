premise_microtron_price = 36
premise_dynaco_price = 68
premise_total_shares = 300
premise_average_price = 40

hypothesis_microtron_price = 36
hypothesis_dynaco_price = 68
hypothesis_total_shares = 300
hypothesis_average_price = 40

# the hypothesis refers to the prices of the stocks mentioned in the premise
if hypothesis_microtron_price >= premise_microtron_price:
    # check if the hypothesis value contradicts the premise value for the price of MicroTron stock
    label = "contradiction"
elif hypothesis_dynaco_price <= premise_dynaco_price:
    # check if the hypothesis value contradicts the premise value for the price of Dynaco stock
    label = "contradiction"
else:
    # the premise gives only an estimate for the prices of the stocks
    # any price of the stocks greater than 'premise_microtron_price' and less than 'premise_dynaco_price' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
