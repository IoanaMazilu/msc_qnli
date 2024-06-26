deposit_premise = 62500
deposit_hypothesis = 62500

# the hypothesis refers to the amount of money deposited by Lucy, which is also mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
