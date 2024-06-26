work_together_days_premise = 12
work_together_days_hypothesis = 72
remaining_work_days_peter = 10

# the hypothesis refers to the number of days they worked together and the number of days Peter worked alone
if work_together_days_hypothesis!= work_together_days_premise:
    # check if the number of days they worked together in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif remaining_work_days_peter!= 10:
    # check if the number of days Peter worked alone in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
