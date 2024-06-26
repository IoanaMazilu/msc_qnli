days_before_work_premise = 7
days_before_work_hypothesis = 1

# the hypothesis refers to the number of days before the work is finished mentioned in the premise
if days_before_work_hypothesis <= days_before_work_premise:
    # check if the estimate of 'days_before_work_hypothesis' contradicts the number of days before the work in the premise
    label = "contradiction"
elif days_before_work_hypothesis > days_before_work_premise:
    # check if the number of days before the work in the hypothesis is more than the number of days before the work in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
