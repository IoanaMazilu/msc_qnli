bonds_purchase_premise = 7000
bonds_purchase_hypothesis = 2000

# the hypothesis talks about the amount of US saving bonds purchased by Robert, which is also mentioned in the premise
if bonds_purchase_hypothesis >= bonds_purchase_premise:
    # check if the hypothesis value contradicts the estimate of less than 'bonds_purchase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of bonds
    # any amount less than 'bonds_purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
