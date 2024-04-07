# Premise: Raman mixed 54 kg of butter at Rs.
# Hypothesis: Raman mixed less than 54 kg of butter at Rs.
# Golden Label: contradiction

butter_kg_premise = 54
butter_kg_hypothesis = 54

# the hypothesis talks about the quantity of butter mixed by Raman, which is also referenced in the premise
if butter_kg_hypothesis < butter_kg_premise:
    # check if the hypothesis value contradicts the weight of butter in the premise
    label = "entailment"
elif butter_kg_hypothesis >= butter_kg_premise:
    # check if the hypothesis value contradicts the estimate of less than 'butter_kg_premise'
    label = "contradiction"
else:
    # any other comparison is considered neutral
    label = "neutral"

print(label)

