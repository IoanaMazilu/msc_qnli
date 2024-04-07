# Premise: If Jim pays less than 70 dollars, how much will Joe have to pay?
# Hypothesis: If Jim pays 30 dollars, how much will Joe have to pay?
# Golden Label: neutral

jim_payment_premise = 70
jim_payment_hypothesis = 30

# the hypothesis talks about the payment made by Jim, which is also referenced in the premise
if jim_payment_hypothesis >= jim_payment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jim_payment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Jim's payment
    # any number of payment less than 'jim_payment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

