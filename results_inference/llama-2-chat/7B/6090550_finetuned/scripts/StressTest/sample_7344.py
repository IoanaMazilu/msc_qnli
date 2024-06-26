percent_price_change_premise = -28
percent_price_change_hypothesis = -68

# the hypothesis refers to the percentage change in crude oil price in the last 3 months, which is also mentioned in the premise
if percent_price_change_hypothesis <= percent_price_change_premise:
    # check if the hypothesis value contradicts the premise value
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, it contradicts the premise
    label = "contradiction"

print(label)
