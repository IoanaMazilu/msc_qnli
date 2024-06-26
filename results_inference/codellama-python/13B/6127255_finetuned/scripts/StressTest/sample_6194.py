pay_per_day_premise = 150
pay_per_day_hypothesis = 150

# the hypothesis refers to the pay per day mentioned in the premise
if pay_per_day_hypothesis >= pay_per_day_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
