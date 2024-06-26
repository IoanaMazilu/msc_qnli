work_hours_monday_wednesday_friday_premise = 2
work_hours_monday_wednesday_friday_hypothesis = 9
work_hours_tuesday_thursday_premise = 5
work_hours_tuesday_thursday_hypothesis = 5

# the hypothesis talks about the number of work hours Mary has per day on Monday, Wednesday and Friday, and Tuesday and Thursday
if work_hours_monday_wednesday_friday_hypothesis <= work_hours_monday_wednesday_friday_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_hours_monday_wednesday_friday_premise'
    label = "contradiction"
elif work_hours_tuesday_thursday_hypothesis!= work_hours_tuesday_thursday_premise:
    # check if the number of work hours on Tuesday and Thursday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of work hours on Monday, Wednesday and Friday
    # any number of work hours greater than 'work_hours_monday_wednesday_friday_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
