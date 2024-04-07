# Premise: Raman mixed 48 kg of butter at Rs.
# Hypothesis: Raman mixed less than 68 kg of butter at Rs.
# Golden Label: entailment

butter_kg_premise = 48
butter_kg_hypothesis = 68

# the hypothesis refers to the quantity of butter mixed by Raman mentioned in the premise
if butter_kg_hypothesis <= butter_kg_premise:
    # check if the hypothesis estimate contradicts the exact quantity of butter in the premise
    label = "contradiction"
elif butter_kg_premise >= butter_kg_hypothesis:
    # check if the exact quantity of butter in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the exact quantity in the premise, we can infer entailment
    label = "entailment"

print(label)

