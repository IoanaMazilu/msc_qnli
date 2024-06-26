average_price_premise = 20
average_price_hypothesis = 60
books_bought_premise = 6
books_bought_hypothesis = 6

# the hypothesis refers to the average price of the books bought and the number of books bought, mentioned in the premise
if average_price_premise >= average_price_hypothesis:
    # check if the average price in the hypothesis contradicts the average price in the premise
    label = "contradiction"
elif books_bought_hypothesis!= books_bought_premise:
    # check if the number of books bought in the hypothesis contradicts the number of books bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
