hardback_books_premise = 10
hardback_books_hypothesis = 10
paperback_books_premise = 60 - hardback_books_premise
paperback_books_hypothesis = 60 - hardback_books_hypothesis

# the hypothesis refers to the number of hardback and paperback books mentioned in the premise
if hardback_books_hypothesis!= hardback_books_premise:
    # check if the number of hardback books in the hypothesis contradicts the number of hardback books reported in the premise
    label = "contradiction"
elif paperback_books_hypothesis!= paperback_books_premise:
    # check if the number of paperback books in the hypothesis contradicts the number of paperback books reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
