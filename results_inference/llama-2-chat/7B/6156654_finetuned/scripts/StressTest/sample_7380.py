books_average_price_premise = 20
books_average_price_hypothesis = 60

# the hypothesis refers to the average price of the books bought by Jithin, which is also mentioned in the premise
if books_average_price_hypothesis <= books_average_price_premise:
    # check if the hypothesis value contradicts the average price in the premise
    label = "contradiction"
elif books_average_price_hypothesis > books_average_price_premise:
    # if the hypothesis value is greater than the average price in the premise, it is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the average price in the premise, it is neutral
    label = "neutral"

print(label)
