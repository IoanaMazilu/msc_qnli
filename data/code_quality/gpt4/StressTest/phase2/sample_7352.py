work_hours_mon_wed_fri_premise = 8
work_hours_mon_wed_fri_hypothesis = 8
work_hours_tue_thu_premise = 6
work_hours_tue_thu_hypothesis = 6

# the hypothesis refers to Sheila's working hours on the same days mentioned in the premise
if work_hours_mon_wed_fri_hypothesis >= work_hours_mon_wed_fri_premise:
    # check if the hypothesis estimate contradicts the number of work hours per day on Monday, Wednesday and Friday reported in the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the number of work hours per day on Tuesday and Thursday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
