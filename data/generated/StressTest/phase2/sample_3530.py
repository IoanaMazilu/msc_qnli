# Premise: Raman mixed 24 kg of butter at Rs.
# Hypothesis: Raman mixed 44 kg of butter at Rs.
# Golden Label: contradiction

butter_kg_premise = 24
butter_kg_hypothesis = 44

# the hypothesis refers to the amount of butter mixed by Raman, mentioned also in the premise
if butter_kg_hypothesis == butter_kg_premise:
    # check if the amount of butter in the hypothesis matches the amount mentioned in the premise
    label = "entailment"
elif butter_kg_hypothesis < butter_kg_premise:
    # check if the amount of butter in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we infer a neutral relation
    label = "neutral"

print(label)

