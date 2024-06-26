premise_saving_amount = 10
hypothesis_saving_amount = 40

# the hypothesis refers to the percentage of saving amount decreased due to loan payment
# the premise mentions a decrease of 10%
if hypothesis_saving_amount <= premise_saving_amount:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of saving amount decreased
    # any percentage greater than 'premise_saving_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
