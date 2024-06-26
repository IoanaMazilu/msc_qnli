jane_age_start_premise = 20
jane_age_start_hypothesis = 40

# the hypothesis refers to Jane's age when she started baby-sitting, which is also mentioned in the premise
if jane_age_start_hypothesis >= jane_age_start_premise:
    # check if the age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis age does not contradict the premise age, we can infer entailment
    label = "entailment"

print(label)
