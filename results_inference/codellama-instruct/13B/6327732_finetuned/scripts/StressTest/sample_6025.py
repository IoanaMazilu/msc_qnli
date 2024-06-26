premise_percentage = 6
hypothesis_percentage = 4

# the hypothesis refers to the percentage of the amount that Dana gives back to her parents each month
# the premise mentions a specific percentage, but does not provide a specific amount
# we can infer entailment if the hypothesis percentage is less than or equal to the premise percentage
if hypothesis_percentage <= premise_percentage:
    label = "entailment"
else:
    label = "neutral"

print(label)
