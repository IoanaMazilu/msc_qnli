work_hours_mon_wed_fri_premise = 5
work_hours_mon_wed_fri_hypothesis = 6
work_hours_tue_thu_premise = 10
work_hours_tue_thu_hypothesis = 10

# the hypothesis refers to the work hours of Catherina on the same days mentioned in the premise
if work_hours_mon_wed_fri_hypothesis!= work_hours_mon_wed_fri_premise:
    # check if the work hours on Monday, Wednesday and Friday in the hypothesis contradicts the work hours reported in the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis!= work_hours_tue_thu_premise:
    # check if the work hours on Tuesday and Thursday in the hypothesis contradicts the work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
