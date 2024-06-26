shop_offer_premise = 30
shop_offer_hypothesis = 80
shirt_price_premise = 
shirt_price_hypothesis = 

# the hypothesis talks about the shop offer for every shirt, which is referenced in the premise
if shop_offer_hypothesis <= shop_offer_premise:
    # check if the hypothesis value contradicts the estimate of'shop_offer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the shop offer
    # any offer greater than'shop_offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
