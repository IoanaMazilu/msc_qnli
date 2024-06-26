store_z_price_premise = 90
store_z_price_hypothesis = 70

# the hypothesis refers to the price of an item at Store Z mentioned in the premise
if store_z_price_premise <= store_z_price_hypothesis:
    # check if the estimate of'store_z_price_hypothesis' contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
