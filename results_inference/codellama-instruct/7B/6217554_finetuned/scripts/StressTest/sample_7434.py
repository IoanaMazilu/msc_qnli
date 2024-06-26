total_price_premise = 90
total_price_hypothesis = 70

# the hypothesis refers to the total price of the item mentioned in the premise
if total_price_hypothesis >= total_price_premise:
    # check if the estimate of 'total_price_hypothesis' contradicts the total price in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
