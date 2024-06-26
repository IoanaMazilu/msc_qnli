total_books_premise = 60
total_books_hypothesis = 40
hardback_books_premise = 10
hardback_books_hypothesis = 10
hardback_price_premise = 20
hardback_price_hypothesis = 20
paperback_price_premise = 10
paperback_price_hypothesis = 10

# the hypothesis refers to the number of purchased books and their type and price mentioned in the premise
if total_books_premise <= total_books_hypothesis:
    # check if the estimate of 'total_books_hypothesis' contradicts the number of purchased books in the premise
    label = "contradiction"
elif hardback_books_premise != hardback_books_hypothesis or hardback_price_premise != hardback_price_hypothesis or paperback_price_premise != paperback_price_hypothesis:
    # check if the number and price of hardback books or the price of paperback books in the hypothesis contradicts the respective information reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
