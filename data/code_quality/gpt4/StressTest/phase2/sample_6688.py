total_books_purchased_premise = 40
total_books_purchased_hypothesis = 60
hardback_books_premise = 10
hardback_books_hypothesis = 10
paperback_books_premise = total_books_purchased_premise - hardback_books_premise
paperback_books_hypothesis = total_books_purchased_hypothesis - hardback_books_hypothesis

# the hypothesis mentions the total number of books, and the number of hardback and paperback books purchased, which are also mentioned in the premise
if total_books_purchased_hypothesis <= total_books_purchased_premise:
    # check if the total number of books purchased in the hypothesis contradicts the estimate of more than 'total_books_purchased_premise'
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise:
    # check if the number of hardback books in the hypothesis contradicts the number of hardback books reported in the premise
    label = "contradiction"
elif paperback_books_hypothesis <= paperback_books_premise:
    # check if the number of paperback books in the hypothesis contradicts the number of paperback books inferred from the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of books and explicitly states the number of hardback and paperback books
    # any total number of books greater than 'total_books_purchased_premise' and any number of hardback and paperback books consistent with the premise,
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
