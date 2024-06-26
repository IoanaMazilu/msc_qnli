father_age_premise = 48
father_age_hypothesis = 28
mother_age_premise = 46
mother_age_hypothesis = 46

# the hypothesis mentions the parents' ages at their children's birth, as stated in the premise
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
