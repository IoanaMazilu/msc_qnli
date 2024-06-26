work_hours_suresh_premise = 9
work_hours_suresh_hypothesis = 9

# the hypothesis refers to the work hours of Suresh mentioned in the premise
if work_hours_suresh_hypothesis < work_hours_suresh_premise:
    # check if 'work_hours_suresh_hypothesis' contradicts the work hours of Suresh in the premise
    label = "contradiction"
elif work_hours_suresh_hypothesis > work_hours_suresh_premise:
    # the hypothesis suggests that Suresh works more than the hours stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
