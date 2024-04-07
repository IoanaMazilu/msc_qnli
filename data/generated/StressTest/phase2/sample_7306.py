# Premise: Mary works more than 2 hours per day on Monday, Wednesday and Friday, and 5 hours per day on Tuesday and Thursday.
# Hypothesis: Mary works 9 hours per day on Monday, Wednesday and Friday, and 5 hours per day on Tuesday and Thursday.
# Golden Label: neutral

work_hours_mon_wed_fri_premise = 2
work_hours_mon_wed_fri_hypothesis = 9
work_hours_tue_thu_premise = 5
work_hours_tue_thu_hypothesis = 5

# the hypothesis refers to the number of work hours per day on specific days of the week mentioned in the premise
if work_hours_mon_wed_fri_hypothesis <= work_hours_mon_wed_fri_premise:
    # check if the number of work hours per day on Monday, Wednesday and Friday in the hypothesis contradicts the number of work hours per day in the premise
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the number of work hours per day on Tuesday and Thursday in the hypothesis contradicts the number of work hours per day in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of work hours per day on Monday, Wednesday and Friday
    # any number of work hours per day greater than 'work_hours_mon_wed_fri_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

