total_books_purchased_premise = 40
total_books_purchased_hypothesis = 60
hardback_books_premise = 10
hardback_books_hypothesis = 10
hardback_price_premise = 20
hardback_price_hypothesis = 20
paperback_books_premise = total_books_purchased_premise - hardback_books_premise
paperback_books_hypothesis = total_books_purchased_hypothesis - hardback_books_hypothesis
paperback_price_premise = 10
paperback_price_hypothesis = 10

# the hypothesis refers to the number of books purchased, the number of hardback and paperback books and their prices
if total_books_purchased_hypothesis >= total_books_purchased_premise:
    # check if the number of books purchased in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise or hardback_price_hypothesis != hardback_price_premise:
    # check if the number or price of hardback books in the hypothesis contradicts the premise
    label = "contradiction"
elif paperback_books_hypothesis != paperback_books_premise or paperback_price_hypothesis != paperback_price_premise:
    # check if the number or price of paperback books in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
