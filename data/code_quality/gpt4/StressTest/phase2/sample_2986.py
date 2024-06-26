purchase_price_premise = 75000
purchase_price_hypothesis = 15000
profit_rate = 20/100

# the hypothesis talks about the purchase price of a house and the profit rate, both referenced also in the premise
if purchase_price_hypothesis >= purchase_price_premise:
    # check if the hypothesis value contradicts the estimate of less than 'purchase_price_premise'
    label = "contradiction"
elif purchase_price_hypothesis <= 0 or profit_rate != 20/100:
    # check if the purchase price in the hypothesis is a valid number and if the profit rate is the same as in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
