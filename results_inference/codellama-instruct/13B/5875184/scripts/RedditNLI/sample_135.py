premise_banks = 30
hypothesis_banks = 117

# the hypothesis and premise mention the number of banks on the problem list
if hypothesis_banks < premise_banks:
    # check if the number of banks in the hypothesis contradicts the number of banks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the valuation
    # any estimate of the percentage in the hypothesis greater or equal to 'percentage_of_valuation_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
