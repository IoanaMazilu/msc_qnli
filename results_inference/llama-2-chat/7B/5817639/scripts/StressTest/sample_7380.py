book_cost_premise = 20
book_cost_hypothesis = 60

# the hypothesis talks about the average price of books, which is also referred to in the premise
if book_cost_hypothesis <= book_cost_premise:
    # check if the hypothesis value contradicts the estimate of the average price in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average price, and any value less than or equal to that estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
