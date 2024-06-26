bonds_purchased_premise = 50
bonds_purchased_hypothesis = 70

# the hypothesis refers to the number of US saving bonds that Robert purchased
# the premise mentions that bonds are sold in $50 or $100 denominations only
# the hypothesis mentions that bonds are sold in $70 or $100 denominations only
# the hypothesis contradicts the premise, as it mentions a different denomination

if bonds_purchased_hypothesis <= bonds_purchased_premise:
    # check if the hypothesis value contradicts the estimate of 'bonds_purchased_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of US saving bonds that Robert purchased
    # any number of US saving bonds greater than 'bonds_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
