work_hours_mon_wed_fri_premise = 5
work_hours_mon_wed_fri_hypothesis = 8
work_hours_tue_thu_premise = 6
work_hours_tue_thu_hypothesis = 6

# the hypothesis refers to the number of work hours per day on Monday, Wednesday and Friday, and Tuesday and Thursday, mentioned in the premise
if work_hours_mon_wed_fri_hypothesis <= work_hours_mon_wed_fri_premise:
    # check if the number of work hours on Monday, Wednesday and Friday in the hypothesis contradicts the estimate of more than 'work_hours_mon_wed_fri_premise'
    label = "contradiction"
elif work_hours_tue_thu_hypothesis!= work_hours_tue_thu_premise:
    # check if the number of work hours on Tuesday and Thursday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of work hours on Monday, Wednesday and Friday
    # any number of work hours greater than 'work_hours_mon_wed_fri_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
