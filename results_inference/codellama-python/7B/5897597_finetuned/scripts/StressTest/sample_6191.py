save_days_premise = 30
save_days_hypothesis = 30
pay_per_day = 125

# the hypothesis refers to the number of days Lexi needed to save and the pay per day, both mentioned in the premise
if save_days_hypothesis <= save_days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
