father_age_premise = 34
father_age_hypothesis = 14
mother_age_premise = 30
mother_age_hypothesis = 30

# the hypothesis mentions the ages of Ayesha's parents at the time of her and her brother's birth
if father_age_hypothesis != father_age_premise:
    # check if the father's age in the hypothesis contradicts the father's age in the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the mother's age in the hypothesis contradicts the mother's age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
