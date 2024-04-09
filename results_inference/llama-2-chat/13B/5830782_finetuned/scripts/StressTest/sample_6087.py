total_working_days_premise = 12
total_working_days_hypothesis = 52
peter_remaining_days_premise = 10
peter_remaining_days_hypothesis = 10

# the hypothesis refers to the total working days and the remaining days Peter worked, mentioned in the premise
if total_working_days_hypothesis < total_working_days_premise:
    # check if the estimate of 'total_working_days_hypothesis' contradicts the number of total working days in the premise
    label = "contradiction"
elif peter_remaining_days_hypothesis!= peter_remaining_days_premise:
    # check if the number of remaining working days in the hypothesis contradicts the number of remaining working days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
