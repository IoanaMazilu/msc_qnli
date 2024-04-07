# Premise: Raman mixed less than 34 kg of butter at Rs.
# Hypothesis: Raman mixed 24 kg of butter at Rs.
# Golden Label: neutral

butter_weight_premise = 34
butter_weight_hypothesis = 24

# the hypothesis refers to the weight of butter mixed by Raman, mentioned also in the premise
if butter_weight_hypothesis >= butter_weight_premise:
    # check if the hypothesis weight contradicts the premise that the weight is less than 'butter_weight_premise'
    label = "contradiction"
elif butter_weight_hypothesis < butter_weight_premise:
    # the premise gives only an estimate for the weight of the butter
    # any weight less than 'butter_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

