passenger_premise = 1
payment_range_premise = 1500
payment_range_hypothesis = 5000

# the hypothesis mentions the payment range for the passenger, which is also referenced in the premise
# however, the hypothesis refers to a specific passenger and a specific trip, which cannot be entailed from the premise
label = "neutral"

print(label)
