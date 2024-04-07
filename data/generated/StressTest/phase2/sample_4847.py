# Premise: Raman mixed 24 kg of butter at Rs.
# Hypothesis: Raman mixed less than 24 kg of butter at Rs.
# Golden Label: contradiction

butter_kg_premise = 24
butter_kg_hypothesis = 24

# the hypothesis talks about the amount of butter mixed by Raman, which is also mentioned in the premise
if butter_kg_hypothesis >= butter_kg_premise:
    # check if the hypothesis value contradicts the estimate of less than 'butter_kg_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)

