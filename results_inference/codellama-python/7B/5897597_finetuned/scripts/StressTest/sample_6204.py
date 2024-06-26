price_per_item_premise = 20
price_per_item_hypothesis = 60

# the hypothesis refers to the price per item mentioned in the premise
if price_per_item_premise >= price_per_item_hypothesis:
    # check if the estimate of 'price_per_item_hypothesis' contradicts the price per item in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
