# Premise: If today in the morning Adams makes a payment of $7, for how many days, including today, will she be connected to the internet without any additional payments, given her initial balance was $0?
# Hypothesis: If today in the morning Adams makes a payment of $more than 1, for how many days, including today, will she be connected to the internet without any additional payments, given her initial balance was $0?
# Golden Label: entailment

payment_today_premise = 7
payment_today_hypothesis = 1

# the hypothesis talks about the payment made by Adams, referenced also in the premise
if payment_today_hypothesis >= payment_today_premise:
    # check if the hypothesis value contradicts the exact payment of 'payment_today_premise'
    label = "contradiction"
else:
    # the premise gives the exact amount of payment
    # any payment greater than 'payment_today_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

