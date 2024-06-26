store_z_price_premise = 90
store_z_price_hypothesis = 50

# the hypothesis refers to the price of an item in Store Z, also mentioned in the premise
if store_z_price_hypothesis >= store_z_price_premise:
    # check if the hypothesis value contradicts the price of 'store_z_price_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
