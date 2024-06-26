work_hours_mon_wed_fri_premise = 2
work_hours_mon_wed_fri_hypothesis = 9
work_hours_tue_thu_premise = 5
work_hours_tue_thu_hypothesis = 5

# the hypothesis refers to the work hours of Mary on Monday, Wednesday, and Friday, and on Tuesday and Thursday, mentioned in the premise
if work_hours_mon_wed_fri_hypothesis <= work_hours_mon_wed_fri_premise:
    # check if the work hours on Monday, Wednesday, and Friday in the hypothesis contradict the estimate of more than 'work_hours_mon_wed_fri_premise'
    label = "contradiction"
elif work_hours_tue_thu_hypothesis!= work_hours_tue_thu_premise:
    # check if the work hours on Tuesday and Thursday in the hypothesis contradict the work hours on Tuesday and Thursday reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the work hours on Monday, Wednesday, and Friday
    # any number of work hours greater than 'work_hours_mon_wed_fri_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
