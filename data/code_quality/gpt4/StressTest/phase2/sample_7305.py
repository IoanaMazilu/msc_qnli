work_hours_mon_wed_fri_premise = 9
work_hours_mon_wed_fri_hypothesis = 2
work_hours_tue_thu_premise = 5
work_hours_tue_thu_hypothesis = 5

# the hypothesis refers to the working hours per day on Monday, Wednesday, and Friday, and also on Tuesday and Thursday, mentioned in the premise
if work_hours_mon_wed_fri_premise <= work_hours_mon_wed_fri_hypothesis:
    # check if the estimate of 'work_hours_mon_wed_fri_hypothesis' contradicts the number of working hours in the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the number of working hours on Tuesday and Thursday in the hypothesis contradicts the number of working hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
