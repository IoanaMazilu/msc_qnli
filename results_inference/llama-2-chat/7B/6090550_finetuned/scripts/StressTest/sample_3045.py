work_hours_mon_wed_fri = 8
work_hours_tue_thu = 6
work_hours_daily = 6

# the hypothesis refers to the daily work hours of Sheila, which are also mentioned in the premise
if work_hours_mon_wed_fri > work_hours_daily:
    # check if the daily work hours in the hypothesis contradict the daily work hours in the premise
    label = "contradiction"
elif work_hours_tue_thu > work_hours_daily:
    # check if the daily work hours in the hypothesis contradict the daily work hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
