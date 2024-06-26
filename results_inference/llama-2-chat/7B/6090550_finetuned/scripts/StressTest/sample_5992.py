gas_price_premise = 2/gallon
gas_price_hypothesis = 4/gallon
gas_amount = 42

# the hypothesis talks about the cost of gas, which is also referenced in the premise
if gas_price_hypothesis <= gas_price_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gas_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the cost of gas
    # any cost of gas greater than 'gas_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
