passengers_premise = 100000
passengers_hypothesis = 100000

# the hypothesis mentions the number of passengers affected by the grounding of Qantas flights, which is also referenced in the premise
# however, the hypothesis does not provide any additional information about the grounding, which cannot be entailed from the premise
label = "neutral"

print(label)
