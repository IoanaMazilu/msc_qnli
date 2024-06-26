hotel_price_premise = 200
hotel_price_hypothesis = 200

# the hypothesis mentions the price of beachfront hotels, which is also referenced in the premise
# however, the hypothesis refers specifically to California, which cannot be entailed from the premise
label = "neutral"

print(label)
