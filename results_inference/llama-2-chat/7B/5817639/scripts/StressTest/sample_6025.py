amount_premise = 1000
amount_hypothesis = 400

# the hypothesis refers to the amount of money Dana will owe her parents after 4 years of college, based on the premise
if amount_hypothesis <= amount_premise:
    # check if the estimate of 'amount_hypothesis' contradicts the amount of money given in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the amount of money, and the hypothesis provides a specific value for the amount owed after 4 years of college
    # any amount of money owed after 4 years of college that is greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
