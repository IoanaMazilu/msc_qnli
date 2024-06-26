work_hours_mon_wed_fri_premise = 5
work_hours_mon_wed_fri_hypothesis = 8
work_hours_tue_thu_premise = 6
work_hours_tue_thu_hypothesis = 6

# the hypothesis refers to Sheila's working hours on the same days as the premise
if work_hours_mon_wed_fri_hypothesis <= work_hours_mon_wed_fri_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_hours_mon_wed_fri_premise'
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the working hours on Tuesday and Thursday in the hypothesis contradicts the same in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the working hours on Monday, Wednesday and Friday
    # any number of hours greater than 'work_hours_mon_wed_fri_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
