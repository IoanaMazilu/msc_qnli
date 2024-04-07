# Premise: Diana works 10 hours per day on Monday, Wednesday and Friday, and 15 hours per day on Tuesday and Thursday.
# Hypothesis: Diana works 30 hours per day on Monday, Wednesday and Friday, and 15 hours per day on Tuesday and Thursday.
# Golden Label: contradiction

work_hours_mon_wed_fri_premise = 10
work_hours_tue_thu_premise = 15
work_hours_mon_wed_fri_hypothesis = 30
work_hours_tue_thu_hypothesis = 15

# the hypothesis refers to the working hours of Diana on the days mentioned in the premise
if work_hours_mon_wed_fri_hypothesis != work_hours_mon_wed_fri_premise:
    # check if the number of work hours on Monday, Wednesday, and Friday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the number of work hours on Tuesday and Thursday in the hypothesis contradicts the number of work hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

