daily_pay_premise = 150
daily_pay_hypothesis = 150

# the hypothesis refers to the daily pay mentioned in the premise
if daily_pay_hypothesis >= daily_pay_premise:
    # check if the estimate of 'daily_pay_hypothesis' contradicts the daily pay in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
