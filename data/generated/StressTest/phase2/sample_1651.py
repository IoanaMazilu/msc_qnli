# Premise: If today in the morning Salley makes a payment of $more than 1, for how many days, including today, will she be connected to the internet without any additional payments, given her initial balance was $0?
# Hypothesis: If today in the morning Salley makes a payment of $7, for how many days, including today, will she be connected to the internet without any additional payments, given her initial balance was $0?
# Golden Label: neutral

payment_premise = 1
payment_hypothesis = 7

# the hypothesis refers to the payment made by Salley, which is also mentioned in the premise
if payment_hypothesis <= payment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'payment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the payment
    # any payment greater than 'payment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

