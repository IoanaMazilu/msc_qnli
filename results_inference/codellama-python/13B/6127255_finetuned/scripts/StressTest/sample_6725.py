from decimal import Decimal

amount_premise = 3600
amount_hypothesis = 3600
interest_rate = 6

# the hypothesis refers to the amount from Anwar mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the amount from the premise
    label = "contradiction"
else:
    # the premise gives the exact amount from Anwar
    # any amount greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
