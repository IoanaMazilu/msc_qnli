bonds_purchased_premise = 50
bonds_purchased_hypothesis = 70

# the hypothesis refers to the number of US saving bonds that Robert purchased
# the premise mentions the denominations in which bonds are sold
if bonds_purchased_hypothesis <= bonds_purchased_premise:
    # check if the hypothesis value contradicts the number of bonds purchased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of bonds purchased
    # any number of bonds greater than 'bonds_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
