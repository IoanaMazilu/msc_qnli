premise_wage = 8.00
premise_tip_rate = 0.30
hypothesis_wage = 8.00
hypothesis_tip_rate = 0.70

# the hypothesis talks about the tip rate, which is a percentage of the cost of the orders
# the premise gives an estimate for the tip rate, but does not provide a specific value
if hypothesis_tip_rate <= premise_tip_rate:
    # check if the hypothesis value contradicts the estimate of less than 'premise_tip_rate'
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip rate
    # any value of the tip rate greater than 'premise_tip_rate' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
