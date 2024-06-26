average_price_premise = 50
average_price_hypothesis = 40

# the hypothesis refers to the average price of the pieces of fruit that Mary keeps, also mentioned in the premise
if average_price_hypothesis!= average_price_premise:
    # check if the average price in the hypothesis contradicts the average price in the premise
    label = "contradiction"
else:
    # if the average prices in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
