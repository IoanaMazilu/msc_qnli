total_books_purchased_premise = 40
hardback_books_premise = 10
paperback_books_premise = total_books_purchased_premise - hardback_books_premise

total_books_purchased_hypothesis = 20
hardback_books_hypothesis = 10
paperback_books_hypothesis = total_books_purchased_hypothesis - hardback_books_hypothesis

# the hypothesis refers to the number of total, hardback and paperback books purchased, which are also mentioned in the premise
if total_books_purchased_hypothesis != total_books_purchased_premise:
    # check if the total number of books purchased in the hypothesis contradicts the premise
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise:
    # check if the number of hardback books in the hypothesis contradicts the premise
    label = "contradiction"
elif paperback_books_hypothesis != paperback_books_premise:
    # check if the number of paperback books in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
