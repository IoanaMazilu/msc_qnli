book_purchased_premise = 60
book_purchased_hypothesis = 60
hardback_book_purchased_premise = 10
hardback_book_purchased_hypothesis = 10
paperback_book_purchased_premise = 50
paperback_book_purchased_hypothesis = 50
book_price_premise = 20
book_price_hypothesis = 20
paperback_book_price_premise = 10
paperback_book_price_hypothesis = 10

# the hypothesis talks about the number of books purchased, the number of hardback books, and the book prices
if book_purchased_hypothesis >= book_purchased_premise:
    # check if the hypothesis value contradicts the number of books purchased in the premise
    label = "contradiction"
elif hardback_book_purchased_hypothesis!= hardback_book_purchased_premise:
    # check if the number of hardback books in the hypothesis contradicts the number of hardback books reported in the premise
    label = "contradiction"
elif paperback_book_purchased_hypothesis!= paperback_book_purchased_premise:
    # check if the number of paperback books in the hypothesis contradicts the number of paperback books reported in the premise
    label = "contradiction"
elif book_price_hypothesis!= book_price_premise:
    # check if the book price in the hypothesis contradicts the book price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
