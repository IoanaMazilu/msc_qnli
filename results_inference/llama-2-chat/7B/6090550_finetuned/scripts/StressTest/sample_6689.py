 books_purchased_premise = 60
books_purchased_hypothesis = 60
hardback_books_premise = 10
hardback_books_hypothesis = 10
paperback_books_premise = 50
paperback_books_hypothesis = 50
book_price_premise = 20
book_price_hypothesis = 20
book_price_paperback_premise = 10
book_price_paperback_hypothesis = 10

# the hypothesis talks about the number of books purchased, the number of hardback and paperback books, and the price of each book
if books_purchased_premise!= books_purchased_hypothesis:
    # check if the number of books purchased in the hypothesis contradicts the number of books purchased in the premise
    label = "contradiction"
elif hardback_books_premise!= hardback_books_hypothesis or paperback_books_premise!= paperback_books_hypothesis:
    # check if the number of hardback or paperback books in the hypothesis contradicts the number of hardback or paperback books in the premise
    label = "contradiction"
elif book_price_premise!= book_price_hypothesis or book_price_paperback_premise!= book_price_paperback_hypothesis:
    # check if the price of each book in the hypothesis contradicts the price of each book in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
