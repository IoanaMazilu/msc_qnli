# Premise: Bookman purchased 30 copies of a new book released recently, 10 of which are hardback and sold for $20 each, and rest are paperback and sold for $10 each.
# Hypothesis: Bookman purchased less than 40 copies of a new book released recently, 10 of which are hardback and sold for $20 each, and rest are paperback and sold for $10 each.
# Golden Label: entailment

total_books_purchased_premise = 30
total_books_purchased_hypothesis = 40
hardback_books_premise = 10
hardback_books_hypothesis = 10
hardback_price_premise = 20
hardback_price_hypothesis = 20
paperback_books_premise = total_books_purchased_premise - hardback_books_premise
paperback_books_hypothesis = total_books_purchased_hypothesis - hardback_books_hypothesis
paperback_price_premise = 10
paperback_price_hypothesis = 10

# the hypothesis refers to the number of books purchased, the number of hardback and paperback books, and their prices, mentioned in the premise
if total_books_purchased_hypothesis < total_books_purchased_premise:
    # check if the estimate of 'total_books_purchased_hypothesis' contradicts the number of total books purchased in the premise
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise or hardback_price_hypothesis != hardback_price_premise:
    # check if the number of hardback books or their price in the hypothesis contradicts the number of hardback books or their price reported in the premise
    label = "contradiction"
elif paperback_books_hypothesis != paperback_books_premise or paperback_price_hypothesis != paperback_price_premise:
    # check if the number of paperback books or their price in the hypothesis contradicts the number of paperback books or their price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

