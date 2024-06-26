total_books_premise = 55
total_books_hypothesis = 25
hardback_books_premise = 10
hardback_books_hypothesis = 10
paperback_books_premise = total_books_premise - hardback_books_premise
paperback_books_hypothesis = total_books_hypothesis - hardback_books_hypothesis

# the hypothesis talks about the number of books purchased, both hardback and paperback, which is also mentioned in the premise
if total_books_hypothesis != total_books_premise:
    # check if the total number of books in the hypothesis contradicts the total number of books in the premise
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise:
    # check if the number of hardback books in the hypothesis contradicts the number of hardback books in the premise
    label = "contradiction"
elif paperback_books_hypothesis != paperback_books_premise:
    # check if the number of paperback books in the hypothesis contradicts the number of paperback books in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
