average_price_premise = 20
average_price_hypothesis = 20

# the hypothesis refers to the average price of the books mentioned in the premise
if average_price_hypothesis >= average_price_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
