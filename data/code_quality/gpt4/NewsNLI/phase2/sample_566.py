passengers_premise = 100000
passengers_hypothesis = 100000

# the hypothesis mentions the number of passengers affected by the groundings, which is also mentioned in the premise
# however, the hypothesis specifies the grounding of Qantas flights, which cannot be inferred from the premise
label = "neutral"

print(label)