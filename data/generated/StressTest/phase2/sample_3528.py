# Premise: Raman mixed 24 kg of butter at Rs.
# Hypothesis: Raman mixed less than 84 kg of butter at Rs.
# Golden Label: entailment

butter_mixed_premise = 24
butter_mixed_hypothesis = 84

# the hypothesis talks about the quantity of butter mixed by Raman, which is also referenced in the premise
if butter_mixed_hypothesis <= butter_mixed_premise:
    # check if the hypothesis value contradicts the exact quantity of 'butter_mixed_premise'
    label = "contradiction"
elif butter_mixed_premise >= butter_mixed_hypothesis:
    # check if the quantity of butter mixed in the premise is more than the quantity mentioned in the hypothesis
    label = "contradiction"
else:
    # the premise gives an exact value for the quantity of butter mixed
    # any quantity less than 'butter_mixed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

