work_hours_monday_wednesday_friday_premise = 5
work_hours_monday_wednesday_friday_hypothesis = 6
work_hours_tuesday_thursday_premise = 10
work_hours_tuesday_thursday_hypothesis = 10

# the hypothesis talks about the number of work hours per day Catherina has on specific days, referenced also in the premise
if work_hours_monday_wednesday_friday_hypothesis!= work_hours_monday_wednesday_friday_premise:
    # check if the number of work hours per day on Monday, Wednesday and Friday in the hypothesis contradicts the number of work hours per day in the premise
    label = "contradiction"
elif work_hours_tuesday_thursday_hypothesis!= work_hours_tuesday_thursday_premise:
    # check if the number of work hours per day on Tuesday and Thursday in the hypothesis contradicts the number of work hours per day in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
