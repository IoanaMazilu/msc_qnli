daily_pay_premise = 150
daily_pay_hypothesis = 150

# the hypothesis refers to the daily pay of Lexi mentioned in the premise
if daily_pay_hypothesis >= daily_pay_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
