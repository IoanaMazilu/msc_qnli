work_hours_mon_wed_fri_premise = 9
work_hours_tue_thu_premise = 5
work_hours_mon_wed_fri_hypothesis = 5
work_hours_tue_thu_hypothesis = 5

# the hypothesis talks about Mary's work hours on different days mentioned in the premise
if work_hours_mon_wed_fri_hypothesis != work_hours_mon_wed_fri_premise:
    # check if the work hours for Monday, Wednesday, Friday in the hypothesis contradict the work hours in the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the work hours for Tuesday, Thursday in the hypothesis contradict the work hours in the premise
    label = "contradiction"
else:
    # if the work hours in the hypothesis do not contradict the work hours in the premise, we can infer entailment
    label = "entailment"

print(label)
