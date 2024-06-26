crude_price_premise = 68
crude_price_hypothesis = 28

if crude_price_hypothesis <= crude_price_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
