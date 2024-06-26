vacation_days_premise = 30
vacation_days_hypothesis = 80
daily_pay_premise = 125
daily_pay_hypothesis = 125

# the hypothesis refers to the number of days needed for Lexi to save and the daily pay of the job mentioned in the premise
if vacation_days_hypothesis <= vacation_days_premise:
    # check if the estimate of 'vacation_days_hypothesis' contradicts the number of vacation days in the premise
    label = "contradiction"
elif daily_pay_hypothesis!= daily_pay_premise:
    # check if the daily pay in the hypothesis contradicts the daily pay reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
