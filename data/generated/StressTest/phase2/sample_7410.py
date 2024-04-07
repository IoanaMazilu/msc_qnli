# Premise: Raman mixed 27 kg of butter at Rs.
# Hypothesis: Raman mixed less than 47 kg of butter at Rs.
# Golden Label: entailment

butter_premise = 27
butter_hypothesis = 47

# The hypothesis talks about the quantity of butter mixed by Raman, which is also mentioned in the premise.
if butter_hypothesis <= butter_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif butter_premise >= butter_hypothesis:
    # check if premise value contradicts the hypothesis which says that the butter is less than 47 kg
    label = "contradiction"
else:
    # any quantity of butter less than 'butter_hypothesis' and more than 'butter_premise' is consistent with the premise
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

