total_books_premise = 75
total_books_hypothesis = 55
hardback_books_premise = 10
hardback_books_hypothesis = 10
price_hardback_premise = 20
price_hardback_hypothesis = 20
paperback_books_premise = total_books_premise - hardback_books_premise
paperback_books_hypothesis = total_books_hypothesis - hardback_books_hypothesis
price_paperback_premise = 10
price_paperback_hypothesis = 10

# the hypothesis talks about the number of books purchased by Bookman, which is also mentioned in the premise
if total_books_hypothesis >= total_books_premise:
    # check if the total number of books purchased according to the hypothesis contradicts the premise
    label = "contradiction"
elif hardback_books_hypothesis != hardback_books_premise or price_hardback_hypothesis != price_hardback_premise:
    # check if the number of hardback books or their price according to the hypothesis contradicts the premise
    label = "contradiction"
elif paperback_books_hypothesis != paperback_books_premise or price_paperback_hypothesis != price_paperback_premise:
    # check if the number of paperback books or their price according to the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
