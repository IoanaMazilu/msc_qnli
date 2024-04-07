# Premise: The workforce of Company Samsung is 60% female.
# Hypothesis: The workforce of Company Samsung is 40% female.
# Golden Label: contradiction

female_workforce_premise = 60
female_workforce_hypothesis = 40

# the hypothesis refers to the percentage of the female workforce in Company Samsung mentioned in the premise
if female_workforce_premise != female_workforce_hypothesis:
    # check if the percentage of female workforce in the hypothesis contradicts the percentage of female workforce reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

