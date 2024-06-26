days_needed_vacation_premise = 30
days_needed_vacation_hypothesis = 30
pay_per_day_premise = 125
pay_per_day_hypothesis = 125

# the hypothesis refers to the number of days needed for a vacation and the pay per day at the job mentioned in the premise
if days_needed_vacation_hypothesis <= days_needed_vacation_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_needed_vacation_premise'
    label = "contradiction"
elif pay_per_day_hypothesis!= pay_per_day_premise:
    # check if the pay per day in the hypothesis contradicts the pay per day reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'days_needed_vacation_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
