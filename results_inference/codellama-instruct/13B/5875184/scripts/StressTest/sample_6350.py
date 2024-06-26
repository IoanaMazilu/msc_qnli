premise_months = 4
hypothesis_months = 4
premise_investment = 90000
hypothesis_investment = 90000

# the hypothesis refers to the number of months and the investment amount mentioned in the premise
if premise_months == hypothesis_months and premise_investment <= hypothesis_investment:
    # check if the estimate of 'hypothesis_investment' contradicts the investment amount in the premise
    label = "contradiction"
elif premise_months == hypothesis_months and premise_investment > hypothesis_investment:
    # check if the hypothesis value contradicts the investment amount in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of months and the investment amount
    # any number of months greater than 'premise_months' and any investment amount greater than 'premise_investment' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
