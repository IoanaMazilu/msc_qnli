price_premise = 90
price_hypothesis = 70

# the hypothesis refers to the price of an item in Store Z mentioned in the premise
if price_premise <= price_hypothesis:
    # check if the estimate of 'price_hypothesis' contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
