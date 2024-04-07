# Premise: Sheila works 8 hours per day on Monday, Wednesday and Friday, and 6 hours per day on Tuesday and Thursday.
# Hypothesis: Sheila works 2 hours per day on Monday, Wednesday and Friday, and 6 hours per day on Tuesday and Thursday.
# Golden Label: contradiction

work_hours_mon_wed_fri_premise = 8
work_hours_tue_thu_premise = 6
work_hours_mon_wed_fri_hypothesis = 2
work_hours_tue_thu_hypothesis = 6

# the hypothesis refers to the working hours of Sheila on the same days mentioned in the premise
if work_hours_mon_wed_fri_hypothesis > work_hours_mon_wed_fri_premise:
    # check if the hypothesis working hours on Monday, Wednesday and Friday contradict the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the working hours on Tuesday and Thursday in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

