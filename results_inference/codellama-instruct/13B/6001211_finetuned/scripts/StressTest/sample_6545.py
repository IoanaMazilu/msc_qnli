father_age_premise = 38
father_age_hypothesis = 18
mother_age_premise = 36
mother_age_hypothesis = 36

# the hypothesis refers to the ages of Ayesha's parents when she and her brother were born
if father_age_hypothesis!= father_age_premise:
    # check if the father's age in the hypothesis contradicts the father's age in the premise
    label = "contradiction"
elif mother_age_hypothesis!= mother_age_premise:
    # check if the mother's age in the hypothesis contradicts the mother's age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
