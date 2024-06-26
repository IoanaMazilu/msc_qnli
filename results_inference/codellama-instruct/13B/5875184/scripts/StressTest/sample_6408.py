shop_offer_premise = 20
shop_offer_hypothesis = 80
shirt_price_premise = 100
shirt_price_hypothesis = 100

# the hypothesis talks about the percentage of discount offered by the shop
if shop_offer_hypothesis >= shop_offer_premise:
    # check if the hypothesis value contradicts the estimate of less than'shop_offer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of discount offered by the shop
    # any percentage of discount less than'shop_offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
