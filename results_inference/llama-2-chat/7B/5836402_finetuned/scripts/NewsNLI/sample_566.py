affected_passengers_premise = 100000
affected_passengers_hypothesis = 100000

# the hypothesis mentions the number of passengers affected by the grounding, which is also referenced in the premise
# however, the hypothesis refers to the grounding of Qantas flights, which cannot be entailed from the premise
label = "neutral"

print(label)
