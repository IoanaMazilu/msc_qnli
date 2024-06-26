days_saved_premise = 30
days_saved_hypothesis = 30
daily_pay_premise = 125
daily_pay_hypothesis = 125

# the hypothesis refers to the number of days Lexi saved and the daily pay mentioned in the premise
if days_saved_hypothesis <= days_saved_premise:
    # check if the estimate of 'days_saved_hypothesis' contradicts the number of days saved in the premise
    label = "contradiction"
elif daily_pay_hypothesis!= daily_pay_premise:
    # check if the daily pay in the hypothesis contradicts the daily pay reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days saved
    # any number of days greater than 'days_saved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
