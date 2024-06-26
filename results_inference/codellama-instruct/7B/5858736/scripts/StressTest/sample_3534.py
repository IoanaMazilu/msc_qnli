tshirt_price_premise = 8
tshirt_price_hypothesis = 3

if tshirt_price_hypothesis <= tshirt_price_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
