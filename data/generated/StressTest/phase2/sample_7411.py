# Premise: Raman mixed less than 47 kg of butter at Rs.
# Hypothesis: Raman mixed 27 kg of butter at Rs.
# Golden Label: neutral

butter_kg_premise = 47
butter_kg_hypothesis = 27

# the hypothesis refers to the quantity of butter mixed by Raman, which is also mentioned in the premise
if butter_kg_hypothesis >= butter_kg_premise:
    # check if the quantity of butter in the hypothesis contradicts the estimation of less than 'butter_kg_premise'
    label = "contradiction"
elif butter_kg_hypothesis < butter_kg_premise:
    # the premise gives only an estimate for the quantity of butter
    # any quantity of butter less than 'butter_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

