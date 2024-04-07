# Premise: Bookman purchased 30 copies of a new book released recently, 10 of which are hardback and sold for $20 each, and rest are paperback and sold for $10 each.
# Hypothesis: Bookman purchased less than 30 copies of a new book released recently, 10 of which are hardback and sold for $20 each, and rest are paperback and sold for $10 each.
# Golden Label: contradiction

total_books_premise = 30
total_books_hypothesis = 30
hardback_books_premise = 10
hardback_books_hypothesis = 10
paperback_books_premise = total_books_premise - hardback_books_premise
paperback_books_hypothesis = total_books_hypothesis - hardback_books_hypothesis

# the hypothesis talks about the total number of books, the number of hardback and paperback books, as mentioned in the premise
if total_books_hypothesis >= total_books_premise:
    # check if the total number of books in the hypothesis contradicts the total number of books mentioned in the premise
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise:
    # check if the number of hardback books in the hypothesis contradicts the number of hardback books reported in the premise
    label = "contradiction"
elif paperback_books_hypothesis != paperback_books_premise:
    # check if the number of paperback books in the hypothesis contradicts the number of paperback books reported in the premise
    label = "contradiction"
else:
    # all the conditions for contradiction have been checked, so if none of them is fulfilled, we can infer entailment
    label = "entailment"

print(label)

