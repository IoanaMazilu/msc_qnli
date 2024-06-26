work_hours_mon_wed_fri_premise = 2
work_hours_mon_wed_fri_hypothesis = 9
work_hours_tue_thu_premise = 5
work_hours_tue_thu_hypothesis = 5

# the hypothesis talks about the number of hours Mary works per day, which is also referenced in the premise
if work_hours_mon_wed_fri_hypothesis <= work_hours_mon_wed_fri_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_hours_mon_wed_fri_premise'
    label = "contradiction"
elif work_hours_tue_thu_hypothesis!= work_hours_tue_thu_premise:
    # check if the number of hours Mary works on Tuesday and Thursday in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Mary works on Monday, Wednesday and Friday
    # any number of hours greater than 'work_hours_mon_wed_fri_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
