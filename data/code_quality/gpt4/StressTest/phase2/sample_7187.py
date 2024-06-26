hours_worked_mon_wed_fri_premise = 5
hours_worked_tue_thu_premise = 10

hours_worked_mon_wed_fri_hypothesis = 6
hours_worked_tue_thu_hypothesis = 10

# the hypothesis refers to the hours Catherina worked per day on Monday, Wednesday, Friday and Tuesday, Thursday
if hours_worked_mon_wed_fri_hypothesis != hours_worked_mon_wed_fri_premise:
    # check if the hours worked on Monday, Wednesday and Friday in the hypothesis contradicts the hours worked on the same days in the premise
    label = "contradiction"
elif hours_worked_tue_thu_hypothesis != hours_worked_tue_thu_premise:
    # check if the hours worked on Tuesday and Thursday in the hypothesis contradicts the hours worked on the same days in the premise
    label = "contradiction"
else:
    # if the hours worked on each day in the hypothesis do not contradict the hours worked on each day in the premise, we can infer entailment
    label = "entailment"

print(label)
