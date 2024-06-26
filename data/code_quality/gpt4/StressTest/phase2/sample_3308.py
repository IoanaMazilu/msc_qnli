gas_price_premise = 4
gas_price_hypothesis = 4

# the hypothesis talks about the cost of gas referenced in the premise
if gas_price_hypothesis != gas_price_premise:
    # check if the gas price mentioned in the hypothesis contradicts the gas price in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are the same
    label = "entailment"

print(label)
