calculator_price_premise = 10
calculator_price_hypothesis = 30

# the hypothesis talks about the discount percentage, referenced also in the premise
if calculator_price_hypothesis <= calculator_price_premise:
    # check if the hypothesis value contradicts the estimate of more than 'calculator_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount percentage
    # any percentage greater than 'calculator_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
