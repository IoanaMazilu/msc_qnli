premise_hours_monday = 2
premise_hours_wednesday = 2
premise_hours_friday = 2
premise_hours_tuesday = 5
premise_hours_thursday = 5

hypothesis_hours_monday = 9
hypothesis_hours_wednesday = 9
hypothesis_hours_friday = 9
hypothesis_hours_tuesday = 5
hypothesis_hours_thursday = 5

# the hypothesis refers to the number of hours worked per day on each day of the week
if hypothesis_hours_monday > premise_hours_monday or hypothesis_hours_wednesday > premise_hours_wednesday or hypothesis_hours_friday > premise_hours_friday:
    # check if the hypothesis value contradicts the estimate of more than 'premise_hours_monday', 'premise_hours_wednesday' or 'premise_hours_friday'
    label = "contradiction"
elif hypothesis_hours_tuesday!= premise_hours_tuesday or hypothesis_hours_thursday!= premise_hours_thursday:
    # check if the number of hours worked on Tuesday and Thursday in the hypothesis contradicts the number of hours worked on those days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked per day on each day of the week
    # any number of hours greater than 'premise_hours_monday', 'premise_hours_wednesday', 'premise_hours_friday', 'premise_hours_tuesday' and 'premise_hours_thursday' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
