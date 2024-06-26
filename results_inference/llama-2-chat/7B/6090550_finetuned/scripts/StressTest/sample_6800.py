y = 5000
purchase_premise = 4000

# the hypothesis talks about the purchase of US saving bonds by Robert
# the hypothesis value is greater than the purchase value in the premise

if purchase_premise!= y:
    # check if the hypothesis value contradicts the purchase value in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the purchase value in the premise are equal, we can infer entailment
    label = "entailment"

print(label)
