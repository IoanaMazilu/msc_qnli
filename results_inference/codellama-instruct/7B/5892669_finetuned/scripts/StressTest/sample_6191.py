save_days_premise = 30
save_days_hypothesis = 30
daily_pay_premise = 125
daily_pay_hypothesis = 125

# the hypothesis refers to the number of days Lexi needed to save and the daily pay, mentioned in the premise
if save_days_hypothesis <= save_days_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif daily_pay_hypothesis!= daily_pay_premise:
    # check if the daily pay in the hypothesis contradicts the daily pay reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
