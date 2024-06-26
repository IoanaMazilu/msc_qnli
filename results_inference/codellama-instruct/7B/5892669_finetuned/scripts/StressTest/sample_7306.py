work_hours_mon_wed_fri_premise = 2
work_hours_mon_wed_fri_hypothesis = 9
work_hours_tue_thu_premise = 5
work_hours_tue_thu_hypothesis = 5

# the hypothesis refers to the work hours of Mary mentioned in the premise
if work_hours_mon_wed_fri_hypothesis <= work_hours_mon_wed_fri_premise:
    # check if the estimate of 'work_hours_mon_wed_fri_hypothesis' contradicts the number of work hours in the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis!= work_hours_tue_thu_premise:
    # check if the number of work hours on Tuesday and Thursday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the work hours
    # any number of work hours greater than 'work_hours_mon_wed_fri_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)