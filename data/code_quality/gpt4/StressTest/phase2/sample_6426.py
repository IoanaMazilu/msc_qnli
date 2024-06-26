price_premise = 450
price_hypothesis = 750

# the hypothesis refers to the price of an item sold to George, mentioned in the premise
if price_premise >= price_hypothesis:
    # check if the price in the premise contradicts the estimate of less than 'price_hypothesis'
    label = "contradiction"
else:
    # the price in the premise is less than 'price_hypothesis'
    label = "entailment"

print(label)
