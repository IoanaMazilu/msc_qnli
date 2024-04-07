# Premise: Raman mixed 54 kg of butter at Rs.
# Hypothesis: Raman mixed more than 14 kg of butter at Rs.
# Golden Label: entailment

butter_premise = 54
butter_hypothesis = 14

# the hypothesis refers to the quantity of butter mentioned in the premise
if butter_premise <= butter_hypothesis:
    # check if the estimate of 'butter_hypothesis' contradicts the quantity of butter in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

