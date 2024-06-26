work_hours_monday_wednesday_friday = 5
work_hours_tuesday_thursday = 10
work_hours_monday_wednesday_friday_hypothesis = 6

# the hypothesis refers to the number of hours Catherina works on Monday, Wednesday and Friday, which is also mentioned in the premise
if work_hours_monday_wednesday_friday!= work_hours_monday_wednesday_friday_hypothesis:
    # check if the number of hours Catherina works on Monday, Wednesday and Friday in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
elif work_hours_tuesday_thursday!= work_hours_tuesday_thursday_hypothesis:
    # check if the number of hours Catherina works on Tuesday and Thursday in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
