monday_wednesday_friday_hours_premise = [9, 9, 9]
tuesday_thursday_hours_premise = [5, 5]
monday_wednesday_friday_hours_hypothesis = [5, 5, 5]
tuesday_thursday_hours_hypothesis = [5, 5]

# the hypothesis refers to the hours Mary works on Monday, Wednesday, Friday and Tuesday and Thursday, mentioned in the premise
if monday_wednesday_friday_hours_hypothesis!= monday_wednesday_friday_hours_premise:
    # check if the number of hours Mary works on Monday, Wednesday, Friday in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
elif tuesday_thursday_hours_hypothesis!= tuesday_thursday_hours_premise:
    # check if the number of hours Mary works on Tuesday and Thursday in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
