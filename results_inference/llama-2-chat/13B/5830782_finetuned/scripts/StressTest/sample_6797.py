deposit_premise = 62500
deposit_hypothesis = 62500

# the hypothesis refers to the amount of money Lucy deposited, which is also mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the hypothesis value contradicts the premise that Lucy deposited exactly 'deposit_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it can be inferred as entailment
    label = "entailment"

print(label)
