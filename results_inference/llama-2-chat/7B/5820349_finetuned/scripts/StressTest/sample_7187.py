work_hours_mon_wed_fri_premise = 5
work_hours_tue_thu_premise = 10
work_hours_mon_wed_fri_hypothesis = 6
work_hours_tue_thu_hypothesis = 10

# the hypothesis refers to the number of work hours per day on Monday, Wednesday and Friday, and Tuesday and Thursday
if work_hours_mon_wed_fri_premise!= work_hours_mon_wed_fri_hypothesis:
    # check if the number of work hours on Monday, Wednesday and Friday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
elif work_hours_tue_thu_premise!= work_hours_tue_thu_hypothesis:
    # check if the number of work hours on Tuesday and Thursday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
