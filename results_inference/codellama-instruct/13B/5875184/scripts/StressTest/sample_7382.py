books_bought_premise = 6
books_bought_hypothesis = 6
average_price_premise = 20
average_price_hypothesis = 20

# the hypothesis refers to the number of books and the average price mentioned in the premise
if books_bought_premise == books_bought_hypothesis and average_price_premise <= average_price_hypothesis:
    # check if the estimate of 'average_price_hypothesis' contradicts the average price in the premise
    label = "contradiction"
elif books_bought_hypothesis!= books_bought_premise or average_price_hypothesis > average_price_premise:
    # check if the number of books or the average price in the hypothesis contradicts the number of books or the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
