monday_wednesday_friday_hours_premise = 5
monday_wednesday_friday_hours_hypothesis = 6
tuesday_thursday_hours_premise = 10
tuesday_thursday_hours_hypothesis = 10

# the hypothesis refers to the hours Catherina works, which are also mentioned in the premise
if monday_wednesday_friday_hours_hypothesis!= monday_wednesday_friday_hours_premise:
    # check if the number of hours Catherina works on Monday, Wednesday, and Friday in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
elif tuesday_thursday_hours_hypothesis!= tuesday_thursday_hours_premise:
    # check if the number of hours Catherina works on Tuesday and Thursday in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
