premise_debt = 57
hypothesis_debt = 57

# the hypothesis and premise mention the same amount of debt
if premise_debt!= hypothesis_debt:
    # check if the amount of debt in the hypothesis contradicts the amount of debt in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of debt
    # any estimate of the amount of debt in the hypothesis greater or equal to 'premise_debt' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
