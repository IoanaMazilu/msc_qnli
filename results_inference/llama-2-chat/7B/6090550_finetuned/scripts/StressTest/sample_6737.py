work_days_rohit = 12
work_days_rohan = 6
total_work_days = work_days_rohit + work_days_rohan
total_work_days_hypothesis = 62

# the hypothesis refers to the number of days required to complete a work by Rohit and Rohan
if total_work_days_hypothesis!= total_work_days:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
