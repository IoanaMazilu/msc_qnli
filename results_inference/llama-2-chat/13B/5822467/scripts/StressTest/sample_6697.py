premise_amount = 5000
hypothesis_amount = 2000

# the premise mentions a specific amount, while the hypothesis gives a range
if hypothesis_amount < premise_amount:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif hypothesis_amount == premise_amount:
    # the hypothesis value is consistent with the premise value
    label = "entailment"
else:
    # the premise gives a specific amount, while the hypothesis gives a range
    # any amount within the range is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
