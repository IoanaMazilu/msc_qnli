total_books_purchased_premise = 60
total_books_purchased_hypothesis = 40
hardback_books_premise = 10
hardback_books_hypothesis = 10
paperback_books_premise = 50
paperback_books_hypothesis = 50

# the hypothesis refers to the total number of books purchased, the number of hardback and paperback books mentioned in the premise
if total_books_purchased_premise <= total_books_purchased_hypothesis:
    # check if the estimate of 'total_books_purchased_hypothesis' contradicts the number of total books purchased in the premise
    label = "contradiction"
elif hardback_books_hypothesis!= hardback_books_premise:
    # check if the number of hardback books in the hypothesis contradicts the number of hardback books reported in the premise
    label = "contradiction"
elif paperback_books_hypothesis!= paperback_books_premise:
    # check if the number of paperback books in the hypothesis contradicts the number of paperback books reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
