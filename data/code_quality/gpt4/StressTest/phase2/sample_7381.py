books_premise = 6
books_hypothesis = 6
avg_price_premise = 60
avg_price_hypothesis = 20

# the hypothesis talks about the number of books and their average price, which are also mentioned in the premise
if books_hypothesis != books_premise:
    # check if the number of books in the hypothesis contradicts the number of books mentioned in the premise
    label = "contradiction"
elif avg_price_hypothesis >= avg_price_premise:
    # check if the average price of books in the hypothesis contradicts the estimate of less than 'avg_price_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate (less than) for the average price of the books
    # the hypothesis average price is lesser than the premise estimate, it doesn't contradict the premise but also cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
