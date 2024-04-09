borrowed_amount_premise = 6500
borrowed_amount_hypothesis = 3500

# the hypothesis refers to the amount of money borrowed annually
if borrowed_amount_hypothesis > borrowed_amount_premise:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif borrowed_amount_hypothesis == borrowed_amount_premise:
    # the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # the premise value is an estimate, and the hypothesis value exceeds the estimate
    label = "entailment"

print(label)
