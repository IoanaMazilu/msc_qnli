# Premise: The border guards and French police are also involved in the hunt for the four men, police said.
# Hypothesis: The four men escaped in a gray-colored vehicle, police said.
# Golden Label: neutral

men_premise = 4
men_hypothesis = 4

# the hypothesis mentions the number of men, which is also referenced in the premise
# however, the hypothesis provides additional information about a gray-colored vehicle, which cannot be entailed from the premise
label = "neutral"

print(label)

