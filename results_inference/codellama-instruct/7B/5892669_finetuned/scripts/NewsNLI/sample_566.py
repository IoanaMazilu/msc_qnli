passengers_premise = 100000
passengers_hypothesis = 100000

# the hypothesis mentions the number of passengers affected by a grounding, which is also referenced in the premise
# however, the hypothesis specifies that the grounding affected Qantas flights, which cannot be entailed from the premise
label = "neutral"

print(label)
