# Premise: Sharmila works 10 hours per day on Monday, Wednesday and Friday, and 8 hours per day on Tuesday and Thursday.
# Hypothesis: Sharmila works less than 80 hours per day on Monday, Wednesday and Friday, and 8 hours per day on Tuesday and Thursday.
# Golden Label: entailment

hours_worked_mon_wed_fri_premise = 10
hours_worked_tue_thu_premise = 8
hours_worked_mon_wed_fri_hypothesis = 80
hours_worked_tue_thu_hypothesis = 8

# the hypothesis refers to the number of hours worked by Sharmila on different days of the week, the same mentioned in the premise
if hours_worked_mon_wed_fri_hypothesis >= hours_worked_mon_wed_fri_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif hours_worked_tue_thu_hypothesis != hours_worked_tue_thu_premise:
    # check if the number of hours worked on Tuesday and Thursday in the hypothesis contradicts the number of hours worked on these days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

