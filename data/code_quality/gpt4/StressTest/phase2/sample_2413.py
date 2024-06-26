total_books_premise = 40
total_books_hypothesis = 30
hardback_books_premise = 10
hardback_books_hypothesis = 10
hardback_price_premise = 20
hardback_price_hypothesis = 20
paperback_price_premise = 10
paperback_price_hypothesis = 10

# the hypothesis refers to the number of total, hardback and paperback books purchased by Bookman
# as well as their prices, all mentioned in the premise
if total_books_hypothesis >= total_books_premise:
    # check if the total number of books in the hypothesis contradicts the premise
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise or hardback_price_hypothesis != hardback_price_premise:
    # check if the number or price of hardback books in the hypothesis contradicts the premise
    label = "contradiction"
elif (total_books_hypothesis-hardback_books_hypothesis)*paperback_price_hypothesis != (total_books_premise-hardback_books_premise)*paperback_price_premise:
    # check if the total price of paperback books in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
