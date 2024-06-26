premise_amount = 288
hypothesis_amount = 888
discount_premise = "Rs." + str(premise_amount)
discount_hypothesis = "Rs." + str(hypothesis_amount)

# check if the hypothesis value contradicts the premise
if hypothesis_amount > premise_amount:
    label = "contradiction"
elif hypothesis_amount == premise_amount:
    # the hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value is less than the premise value, so it can be entailed from the premise
    label = "entailment"

print(label)
