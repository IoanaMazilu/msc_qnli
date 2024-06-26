daily_pay_premise = 150
daily_pay_hypothesis = 150

# the hypothesis refers to the daily pay mentioned in the premise
if daily_pay_hypothesis >= daily_pay_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be explicitly entailed from the premise
    label = "entailment"

print(label)
