daily_pay_premise = 150
daily_pay_hypothesis = 150

# the hypothesis refers to the daily pay of Lexi's new job mentioned in the premise
if daily_pay_hypothesis >= daily_pay_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
