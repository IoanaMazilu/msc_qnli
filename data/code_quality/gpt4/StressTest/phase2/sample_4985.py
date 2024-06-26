father_age_premise = 58
father_age_hypothesis = 18
mother_age_premise = 42
mother_age_hypothesis = 42

# the hypothesis refers to the age of Ayesha's parents when she and her brother were born, also mentioned in the premise
if father_age_hypothesis != father_age_premise:
    # check if the father's age in the hypothesis contradicts the father's age reported in the premise
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the mother's age in the hypothesis contradicts the mother's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
