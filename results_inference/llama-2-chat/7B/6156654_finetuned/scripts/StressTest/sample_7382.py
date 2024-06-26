average_price_premise = 20
average_price_hypothesis = 20

# the hypothesis refers to the average price of the books bought by Jithin
if average_price_premise >= average_price_hypothesis:
    # check if the average price in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the average price in the premise is less than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
