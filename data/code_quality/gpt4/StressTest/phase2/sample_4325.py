average_price_premise = 48
average_price_hypothesis = 38

# the hypothesis refers to the average price of fruit mentioned in the premise
if average_price_hypothesis != average_price_premise:
    # check if the average price in the hypothesis contradicts the average price in the premise
    label = "contradiction"
else:
    # if the average prices do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
