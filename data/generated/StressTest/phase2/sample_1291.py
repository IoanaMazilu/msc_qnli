# Premise: Sheila works more than 3 hours per day on Monday, Wednesday and Friday, and 6 hours per day on Tuesday and Thursday.
# Hypothesis: Sheila works 8 hours per day on Monday, Wednesday and Friday, and 6 hours per day on Tuesday and Thursday.
# Golden Label: neutral

work_hours_mon_wed_fri_premise = 3
work_hours_mon_wed_fri_hypothesis = 8
work_hours_tue_thu_premise = 6
work_hours_tue_thu_hypothesis = 6

# the hypothesis talks about the number of work hours of Sheila, referenced also in the premise
if work_hours_mon_wed_fri_hypothesis <= work_hours_mon_wed_fri_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_hours_mon_wed_fri_premise'
    label = "contradiction"
elif work_hours_tue_thu_hypothesis != work_hours_tue_thu_premise:
    # check if the number of work hours on Tuesday and Thursday in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of work hours on Monday, Wednesday and Friday
    # any number of hours greater than 'work_hours_mon_wed_fri_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

