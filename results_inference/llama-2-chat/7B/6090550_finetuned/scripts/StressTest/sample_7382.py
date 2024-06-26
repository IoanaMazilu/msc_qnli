average_price_premise = 20
average_price_hypothesis = 20

# the hypothesis refers to the average price of the books mentioned in the premise
if average_price_hypothesis >= average_price_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_price_hypothesis < average_price_premise:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"
else:
    # if the hypothesis value is the same as the premise value, it is explicitly entailed from the premise
    label = "entailment"

print(label)
