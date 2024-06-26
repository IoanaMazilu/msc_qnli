passengers_affected_premise = 100000
passengers_affected_hypothesis = 100000

# the hypothesis mentions the number of passengers affected by the grounding, which is also referenced in the premise
# however, the hypothesis specifies the type of flights, which cannot be entailed from the premise
label = "neutral"

print(label)
