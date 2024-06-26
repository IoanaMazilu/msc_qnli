work_hours_monday_wednesday_friday_premise = [2, 2, 2]
work_hours_monday_wednesday_friday_hypothesis = [9, 9, 9]
work_hours_tuesday_thursday_premise = [5, 5]
work_hours_tuesday_thursday_hypothesis = [5, 5]

# the hypothesis refers to the number of hours Mary works per day, mentioned in the premise
if work_hours_monday_wednesday_friday_hypothesis!= work_hours_monday_wednesday_friday_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
elif work_hours_tuesday_thursday_hypothesis!= work_hours_tuesday_thursday_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
