capital_belle_premise = 250
capital_belle_hypothesis = 850

# the hypothesis and premise both refer to Belle's capital
if capital_belle_premise != capital_belle_hypothesis:
    # check if the value of Belle's capital in the hypothesis contradicts the value in the premise
    label = "contradiction"
else:
    # if the value of Belle's capital in the hypothesis does not contradict the value in the premise, we have entailment
    label = "entailment"

print(label)
