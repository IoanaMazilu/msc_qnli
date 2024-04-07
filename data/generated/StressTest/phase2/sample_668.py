# Premise: Raman mixed 48 kg of butter at Rs.
# Hypothesis: Raman mixed more than 48 kg of butter at Rs.
# Golden Label: contradiction

butter_weight_premise = 48
butter_weight_hypothesis = 48

# the hypothesis mentions the weight of butter mixed by Raman mentioned in the premise
if butter_weight_hypothesis <= butter_weight_premise:
    # check if the hypothesis estimate contradicts the weight of butter in the premise
    label = "contradiction"
else:
    # the hypothesis states that 'more than butter_weight_premise' was mixed while the premise specifies 'butter_weight_premise'
    # hence, the hypothesis can't be explicitly entailed from the premise
    label = "neutral"

print(label)

