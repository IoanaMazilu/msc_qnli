store_z_price_premise = 90
store_z_price_hypothesis = 70

# the hypothesis refers to the price of an item in Store Z, which is also mentioned in the premise
if store_z_price_premise <= store_z_price_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
