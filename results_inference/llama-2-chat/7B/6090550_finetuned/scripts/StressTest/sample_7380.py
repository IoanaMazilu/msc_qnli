 price_premise = 20
price_hypothesis = 60

# the hypothesis refers to the price of the books, which is also mentioned in the premise
if price_hypothesis <= price_premise:
    # check if the hypothesis value contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
