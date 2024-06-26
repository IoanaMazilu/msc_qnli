aswin_age_premise = 35
sachin_age_premise = 40
sumesh_age_premise = 38
total_age_premise = 93
sum_age_hypothesis = 43

# the hypothesis refers to the sum of ages of 3 people mentioned in the premise
if total_age_premise >= sum_age_hypothesis:
    # check if the estimate of'sum_age_hypothesis' contradicts the total age in the premise
    label = "contradiction"
elif sum_age_hypothesis > total_age_premise:
    # check if the sum of ages in the hypothesis contradicts the total age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
