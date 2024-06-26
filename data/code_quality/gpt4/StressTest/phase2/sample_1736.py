father_age_premise = 40
father_age_hypothesis = 40
mother_age_premise = 32
mother_age_hypothesis = 32

# the hypothesis refers to the ages of Ayesha's parents at certain events mentioned in the premise
if father_age_hypothesis > father_age_premise:
    # check if the claim about the father's age in the hypothesis contradicts the father's age reported in the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the mother's age in the hypothesis contradicts the mother's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
