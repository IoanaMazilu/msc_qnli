average_price_premise = 48
average_price_hypothesis = 78

# the hypothesis refers to the same situation as the premise but with a different average price
if average_price_hypothesis < average_price_premise:
    # check if the average price in the hypothesis contradicts the average price mentioned in the premise
    label = "contradiction"
elif average_price_hypothesis == average_price_premise:
    # check if the average price in the hypothesis is exactly the same as in the premise
    label = "entailment"
else:
    # the premise gives only a specific average price
    # any average price greater than 'average_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
