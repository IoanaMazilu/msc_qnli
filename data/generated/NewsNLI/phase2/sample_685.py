# Premise: There were 155 people aboard, including seven children, she said.
# Hypothesis: 155 people were aboard the Dagestan Airlines flight.
# Golden Label: neutral

people_premise = 155
people_hypothesis = 155

# the hypothesis mentions the number of people aboard, which is also referenced in the premise
# however, the hypothesis specifies the flight as Dagestan Airlines, which cannot be entailed from the premise
label = "neutral"

print(label)

