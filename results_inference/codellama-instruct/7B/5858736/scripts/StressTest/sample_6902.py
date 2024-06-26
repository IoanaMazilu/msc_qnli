shirt_price_premise = 30
shirt_price_hypothesis = 80

if shirt_price_hypothesis <= shirt_price_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
