total_books_premise = 60
hardback_books_premise = 10
hardback_books_price_premise = 20
paperback_books_price_premise = 10

total_books_hypothesis = 60
hardback_books_hypothesis = 10
hardback_books_price_hypothesis = 20
paperback_books_price_hypothesis = 10

# the hypothesis refers to the number of books, the number of hardback books, 
# the price of hardback books and the price of paperback books mentioned in the premise
if total_books_hypothesis >= total_books_premise:
    # check if the estimate of 'total_books_hypothesis' contradicts the number of total books in the premise
    label = "contradiction"
elif hardback_books_hypothesis!= hardback_books_premise or hardback_books_price_hypothesis!= hardback_books_price_premise:
    # check if the number of hardback books or their price in the hypothesis contradicts the number of hardback books or their price reported in the premise
    label = "contradiction"
elif paperback_books_price_hypothesis!= paperback_books_price_premise:
    # check if the price of paperback books in the hypothesis contradicts the price of paperback books reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
