total_books_purchased_premise = 55
total_books_purchased_hypothesis = 75
hardback_books_premise = 10
hardback_books_hypothesis = 10
paperback_books_premise = total_books_purchased_premise - hardback_books_premise
paperback_books_hypothesis = total_books_purchased_hypothesis - hardback_books_hypothesis

# the hypothesis refers to the number of purchased books, hardback and paperback, and their prices mentioned in the premise
if total_books_purchased_hypothesis < total_books_purchased_premise:
    # check if the total number of books purchased in the hypothesis contradicts the number of books purchased in the premise
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise or paperback_books_hypothesis != paperback_books_premise:
    # check if the number of hardback or paperback books purchased in the hypothesis contradicts the number of hardback or paperback books purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
