father_age_premise = 38
father_age_hypothesis = 28
mother_age_premise = 36
mother_age_hypothesis = 36

# the hypothesis refers to the ages of Ayesha's parents mentioned in the premise
if father_age_premise <= father_age_hypothesis:
    # check if the age of the father in hypothesis contradicts the father's age in the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the mother's age in the hypothesis contradicts her age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
