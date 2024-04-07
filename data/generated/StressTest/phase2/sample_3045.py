# Premise: Sheila works 8 hours per day on Monday, Wednesday and Friday, and 6 hours per day on Tuesday and Thursday.
# Hypothesis: Sheila works more than 5 hours per day on Monday, Wednesday and Friday, and 6 hours per day on Tuesday and Thursday.
# Golden Label: entailment

work_hours_mon_wed_fri_premise = 8
work_hours_mon_wed_fri_hypothesis = 5
work_hours_tue_thu_premise = 6
work_hours_tue_thu_hypothesis = 6

# the hypothesis refers to the number of hours Sheila works on certain days, same as the premise
if work_hours_mon_wed_fri_premise <= work_hours_mon_wed_fri_hypothesis:
    # check if the hours Sheila works on Monday, Wednesday and Friday in the hypothesis contradicts the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the hours Sheila works on Tuesday and Thursday in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

