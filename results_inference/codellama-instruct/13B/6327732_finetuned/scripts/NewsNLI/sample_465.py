fines_premise = 10000
fines_hypothesis = 4500000

# the hypothesis mentions the maximum amount of outstanding fines, which is also referenced in the premise
# however, the hypothesis mentions the amount in USD, while the premise mentions the amount in CNY
# this difference cannot be entailed from the premise
label = "neutral"

print(label)
