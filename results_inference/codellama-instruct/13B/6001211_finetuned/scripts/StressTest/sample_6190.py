save_days_premise = 80
save_days_hypothesis = 30
daily_pay_premise = 125
daily_pay_hypothesis = 125

# the hypothesis refers to the number of days Lexi needed to save and the daily pay, both mentioned in the premise
if save_days_hypothesis >= save_days_premise:
    # check if the number of'save_days_hypothesis' contradicts the estimate of less than'save_days_premise'
    label = "contradiction"
elif daily_pay_hypothesis!= daily_pay_premise:
    # check if the daily pay in the hypothesis contradicts the daily pay reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Lexi needed to save
    # any number of days less than'save_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
