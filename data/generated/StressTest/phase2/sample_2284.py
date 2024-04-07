# Premise: Bookman purchased less than 60 copies of a new book released recently, 10 of which are hardback and sold for $20 each, and rest are paperback and sold for $10 each.
# Hypothesis: Bookman purchased 40 copies of a new book released recently, 10 of which are hardback and sold for $20 each, and rest are paperback and sold for $10 each.
# Golden Label: neutral

total_books_premise = 60
hardback_books_premise = 10
paperback_books_premise = total_books_premise - hardback_books_premise

total_books_hypothesis = 40
hardback_books_hypothesis = 10
paperback_books_hypothesis = total_books_hypothesis - hardback_books_hypothesis

# the hypothesis refers to the number of total, hardback and paperback books purchased by Bookman, same as the premise
if total_books_hypothesis >= total_books_premise:
    # check if the total number of books in the hypothesis contradicts the estimate of less than 'total_books_premise'
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise or paperback_books_hypothesis > paperback_books_premise:
    # check if the number of hardback or paperback books in the hypothesis contradicts the number of hardback or paperback books in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

