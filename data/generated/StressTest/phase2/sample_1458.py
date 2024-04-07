# Premise: Sheila works 8 hours per day on Monday, Wednesday and Friday, and 6 hours per day on Tuesday and Thursday.
# Hypothesis: Sheila works more than 4 hours per day on Monday, Wednesday and Friday, and 6 hours per day on Tuesday and Thursday.
# Golden Label: entailment

work_hours_mon_wed_fri_premise = 8
work_hours_mon_wed_fri_hypothesis = 4
work_hours_tue_thu_premise = 6
work_hours_tue_thu_hypothesis = 6

# the hypothesis refers to the number of work hours per day mentioned in the premise
if work_hours_mon_wed_fri_premise <= work_hours_mon_wed_fri_hypothesis:
    # check if the estimate of 'work_hours_mon_wed_fri_hypothesis' contradicts the number of work hours in the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the number of work hours on Tuesday and Thursday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

