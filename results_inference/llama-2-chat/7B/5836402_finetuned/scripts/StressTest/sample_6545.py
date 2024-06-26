father_age_premise = 38
mother_age_premise = 36
brother_age_premise = 4
father_age_hypothesis = 18
mother_age_hypothesis = 36
brother_age_hypothesis = 4

# the hypothesis refers to the ages of Ayesha's father, mother, and brother mentioned in the premise
if father_age_premise!= father_age_hypothesis:
    # check if the father's age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif mother_age_hypothesis!= mother_age_premise:
    # check if the mother's age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif brother_age_hypothesis!= brother_age_premise:
    # check if the brother's age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
