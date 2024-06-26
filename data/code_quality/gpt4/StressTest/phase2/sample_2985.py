purchase_price_premise = 15000
purchase_price_hypothesis = 75000
profit_percentage_premise = 20
profit_percentage_hypothesis = 20

# the hypothesis refers to the purchase price and profit percentage mentioned in the premise
if purchase_price_hypothesis <= purchase_price_premise:
    # check if the hypothesis value contradicts the specific purchase price given in the premise
    label = "contradiction"
elif profit_percentage_hypothesis != profit_percentage_premise:
    # check if the profit percentage in the hypothesis contradicts the profit percentage in the premise
    label = "contradiction"
else: 
    # if the hypothesis values do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
