# Premise: Raman mixed 44 kg of butter at Rs.
# Hypothesis: Raman mixed more than 44 kg of butter at Rs.
# Golden Label: contradiction

butter_kg_premise = 44
butter_kg_hypothesis = 44

# the hypothesis refers to the amount of butter mentioned in the premise
if butter_kg_hypothesis >= butter_kg_premise:
    # check if the value of 'butter_kg_hypothesis' contradicts the exact amount of butter in the premise
    label = "contradiction"
else:
    # the hypothesis value and the premise value are the same, thus it isn't more
    label = "neutral"

print(label)

