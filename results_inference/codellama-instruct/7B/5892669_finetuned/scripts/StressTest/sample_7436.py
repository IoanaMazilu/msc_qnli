store_z_price_premise = 90
store_z_price_hypothesis = 90

# the hypothesis refers to the price of an item at Store Z mentioned in the premise
if store_z_price_hypothesis >= store_z_price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
