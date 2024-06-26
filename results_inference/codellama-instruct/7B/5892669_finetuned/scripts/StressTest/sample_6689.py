total_books_premise = 60
hardback_books_premise = 10
hardback_price_premise = 20
paperback_books_premise = total_books_premise - hardback_books_premise
paperback_price_premise = 10

total_books_hypothesis = 60
hardback_books_hypothesis = 10
hardback_price_hypothesis = 20
paperback_books_hypothesis = total_books_hypothesis - hardback_books_hypothesis
paperback_price_hypothesis = 10

# the hypothesis refers to the total number of books, hardback and paperback books, and their prices mentioned in the premise
if total_books_hypothesis >= total_books_premise:
    # check if the total number of books in the hypothesis contradicts the total number of books in the premise
    label = "contradiction"
elif hardback_books_hypothesis!= hardback_books_premise or hardback_price_hypothesis!= hardback_price_premise:
    # check if the number of hardback books or their price in the hypothesis contradicts the number of hardback books or their price in the premise
    label = "contradiction"
elif paperback_books_hypothesis!= paperback_books_premise or paperback_price_hypothesis!= paperback_price_premise:
    # check if the number of paperback books or their price in the hypothesis contradicts the number of paperback books or their price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
