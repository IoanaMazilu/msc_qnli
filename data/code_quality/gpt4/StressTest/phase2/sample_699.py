female_workforce_percentage_premise = 60
female_workforce_percentage_hypothesis = 50

# the hypothesis refers to the percentage of female workforce in Samsung, also mentioned in the premise
if female_workforce_percentage_premise <= female_workforce_percentage_hypothesis:
    # check if the percentage of female workforce in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the percentage of female workforce in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
