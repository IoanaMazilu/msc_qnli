# Premise: Raman mixed less than 44 kg of butter at Rs.
# Hypothesis: Raman mixed 34 kg of butter at Rs.
# Golden Label: neutral

butter_kg_premise = 44
butter_kg_hypothesis = 34

# the hypothesis talks about the quantity of butter mixed by Raman, which is also mentioned in the premise
if butter_kg_hypothesis >= butter_kg_premise:
    # check if the hypothesis value contradicts the estimate of less than 'butter_kg_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of butter
    # any quantity of butter less than 'butter_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

