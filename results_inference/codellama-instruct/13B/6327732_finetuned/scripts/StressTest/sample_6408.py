shop_offer_premise = 20
shop_offer_hypothesis = 80

# the hypothesis talks about the percentage of discount offered by the shop
if shop_offer_hypothesis >= shop_offer_premise:
    # check if the hypothesis value contradicts the percentage of discount mentioned in the premise
    label = "contradiction"
else:
    # the premise mentions a percentage of discount, but the hypothesis mentions a lower percentage
    # this means that the hypothesis cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
