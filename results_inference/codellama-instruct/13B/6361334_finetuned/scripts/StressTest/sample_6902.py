shop_offer_premise = 30
shop_offer_hypothesis = 80

# the hypothesis refers to the shop offer for every shirt, which is also mentioned in the premise
if shop_offer_hypothesis <= shop_offer_premise:
    # check if the estimate of'shop_offer_hypothesis' contradicts the offer in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the shop offer
    # any offer greater than'shop_offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
