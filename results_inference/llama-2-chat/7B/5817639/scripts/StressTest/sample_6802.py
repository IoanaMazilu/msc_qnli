denominations_premise = ['$less than 70', '$100']
denominations_hypothesis = ['$50', '$100']

# the hypothesis talks about the denominations of bonds, referenced also in the premise
if any(denom in denominations_hypothesis for denom in denominations_premise):
    # if any of the denominations in the hypothesis is also in the premise, it contradicts the premise
    label = "contradiction"
else:
    # if none of the denominations in the hypothesis is in the premise, it can be entailed from the premise
    label = "entailment"

print(label)
