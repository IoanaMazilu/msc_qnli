books_bought_premise = 6
average_price_premise = 20
average_price_hypothesis = 20

# the hypothesis refers to the number of books bought and the average price mentioned in the premise
if average_price_premise >= average_price_hypothesis:
    # check if the estimate of 'average_price_hypothesis' contradicts the average price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)