saving_days_premise = 30
saving_days_hypothesis = 30
daily_pay_premise = 125
daily_pay_hypothesis = 125

# the hypothesis refers to the number of days Lexi needed to save and the daily pay, mentioned in the premise
if saving_days_hypothesis <= saving_days_premise:
    # check if the hypothesis value contradicts the estimate of more than'saving_days_hypothesis' days
    label = "contradiction"
elif daily_pay_hypothesis!= daily_pay_premise:
    # check if the daily pay in the hypothesis contradicts the daily pay reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
