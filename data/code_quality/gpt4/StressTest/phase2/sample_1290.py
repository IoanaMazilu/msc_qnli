work_hours_mon_wed_fri_premise = 8
work_hours_mon_wed_fri_hypothesis = 3
work_hours_tue_thurs_premise = 6
work_hours_tue_thurs_hypothesis = 6

# the hypothesis refers to the number of hours Sheila works on certain days of the week, as stated in the premise
if work_hours_mon_wed_fri_premise <= work_hours_mon_wed_fri_hypothesis:
    # check if the estimate of 'work_hours_mon_wed_fri_hypothesis' contradicts the number of work hours in the premise
    label = "contradiction"
elif work_hours_tue_thurs_hypothesis != work_hours_tue_thurs_premise:
    # check if the number of work hours on Tuesday and Thursday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
