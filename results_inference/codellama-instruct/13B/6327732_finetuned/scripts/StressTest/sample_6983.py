borrowed_money_premise = 6
borrowed_money_hypothesis = 8

# the hypothesis refers to the rate of borrowing money, which is mentioned in the premise
if borrowed_money_hypothesis <= borrowed_money_premise:
    # check if the estimate of 'borrowed_money_hypothesis' contradicts the rate of borrowing money in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate of borrowing money
    # any rate of borrowing money greater than 'borrowed_money_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
