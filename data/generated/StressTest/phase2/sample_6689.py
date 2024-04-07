# Premise: Bookman purchased 60 copies of a new book released recently, 10 of which are hardback and sold for $20 each, and rest are paperback and sold for $10 each.
# Hypothesis: Bookman purchased less than 60 copies of a new book released recently, 10 of which are hardback and sold for $20 each, and rest are paperback and sold for $10 each.
# Golden Label: contradiction

total_books_premise = 60
total_books_hypothesis = 60
hardback_books_premise = 10
hardback_books_hypothesis = 10
hardback_price_premise = 20
hardback_price_hypothesis = 20
paperback_books_premise = total_books_premise - hardback_books_premise
paperback_books_hypothesis = total_books_hypothesis - hardback_books_hypothesis
paperback_price_premise = 10
paperback_price_hypothesis = 10

# the hypothesis talks about the number of total, hardback and paperback books purchased by Bookman, also mentioned in the premise
if total_books_hypothesis >= total_books_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_books_premise'
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise or hardback_price_hypothesis != hardback_price_premise:
    # check if the number or price of hardback books in the hypothesis contradicts the number or price of hardback books reported in the premise
    label = "contradiction"
elif paperback_books_hypothesis != paperback_books_premise or paperback_price_hypothesis != paperback_price_premise:
    # check if the number or price of paperback books in the hypothesis contradicts the number or price of paperback books reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

