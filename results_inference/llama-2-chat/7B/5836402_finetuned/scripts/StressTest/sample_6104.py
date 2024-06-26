jane_age_start_premise = 18
jane_age_start_hypothesis = 58

# the hypothesis refers to Jane's age when she started baby-sitting, which is also mentioned in the premise
if jane_age_start_hypothesis <= jane_age_start_premise:
    # check if the hypothesis value contradicts the estimate of Jane's age when she started baby-sitting in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
