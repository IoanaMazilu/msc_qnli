affected_passengers_premise = 100000
affected_passengers_hypothesis = 100000

# the hypothesis mentions the number of affected passengers, which is also mentioned in the premise
# however, the hypothesis specifies the reason (grounding of Qantas flights), which cannot be entailed from the premise
label = "neutral"

print(label)
