# Premise: Sharmila works 10 hours per day on Monday, Wednesday and Friday, and 8 hours per day on Tuesday and Thursday.
# Hypothesis: Sharmila works less than 10 hours per day on Monday, Wednesday and Friday, and 8 hours per day on Tuesday and Thursday.
# Golden Label: contradiction

work_hours_mon_wed_fri_premise = 10
work_hours_mon_wed_fri_hypothesis = 10
work_hours_tue_thu_premise = 8
work_hours_tue_thu_hypothesis = 8

# the hypothesis refers to the work hours of Sharmila on different days of the week, also mentioned in the premise
if work_hours_mon_wed_fri_hypothesis >= work_hours_mon_wed_fri_premise:
    # check if the hypothesis estimate contradicts the work hours on Mon, Wed, Fri reported in the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the work hours on Tue, Thu in the hypothesis contradicts the work hours on Tue, Thu reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

