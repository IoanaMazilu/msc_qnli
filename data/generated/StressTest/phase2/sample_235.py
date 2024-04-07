# Premise: Raman mixed less than 44 kg of butter at Rs.
# Hypothesis: Raman mixed 24 kg of butter at Rs.
# Golden Label: neutral

butter_kg_premise = 44
butter_kg_hypothesis = 24

# The hypothesis refers to the quantity of butter mixed by Raman, which is also mentioned in the premise
if butter_kg_hypothesis >= butter_kg_premise:
    # check if the quantity in the hypothesis contradicts the estimate of less than 'butter_kg_premise' in the premise
    label = "contradiction"
elif butter_kg_hypothesis < butter_kg_premise:
    # the premise gives only an estimate for the quantity of butter
    # any quantity less than 'butter_kg_premise' is consistent with the premise, and can be explicitly entailed from the premise
    label = "entailment"

print(label)

