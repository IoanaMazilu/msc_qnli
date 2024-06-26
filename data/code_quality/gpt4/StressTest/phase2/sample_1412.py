raj_age_premise = 20
raj_age_hypothesis = 40

# the hypothesis and premise both refer to the comparison of ages between Raj and Hema at specific ages of Raj
if raj_age_premise != raj_age_hypothesis:
    # check if the age of Raj in the hypothesis contradicts the age of Raj in the premise
    label = "contradiction"
else:
    # if the age of Raj in the hypothesis does not contradict the age of Raj in the premise, we cannot infer any entailment or neutrality without knowing Hema's age
    label = "neutral"

print(label)
