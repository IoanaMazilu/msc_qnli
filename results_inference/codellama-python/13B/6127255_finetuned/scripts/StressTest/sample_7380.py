books_bought_premise = 6
books_bought_hypothesis = 6
average_price_premise = 20
average_price_hypothesis = 60

# the hypothesis refers to the number of books bought and their average price mentioned in the premise
if books_bought_hypothesis!= books_bought_premise:
    # check if the number of books bought in the hypothesis contradicts the number of books bought reported in the premise
    label = "contradiction"
elif average_price_premise > average_price_hypothesis:
    # check if the average price in the premise contradicts the estimate of less than 'average_price_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
