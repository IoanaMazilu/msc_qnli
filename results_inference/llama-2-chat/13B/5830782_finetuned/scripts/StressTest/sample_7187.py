monday_wednesday_friday_hours_premise = 5
tuesday_thursday_hours_premise = 10

monday_wednesday_friday_hours_hypothesis = 6
tuesday_thursday_hours_hypothesis = 10

# the hypothesis talks about the number of hours Catherina works each day, which is also mentioned in the premise
if monday_wednesday_friday_hours_hypothesis!= monday_wednesday_friday_hours_premise:
    # check if the number of hours Catherina works on Monday, Wednesday, and Friday in the hypothesis contradicts the number of hours mentioned in the premise
    label = "contradiction"
elif tuesday_thursday_hours_hypothesis!= tuesday_thursday_hours_premise:
    # check if the number of hours Catherina works on Tuesday and Thursday in the hypothesis contradicts the number of hours mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, but the days of the week are not specified, we infer neutrality
    label = "neutral"

print(label)
