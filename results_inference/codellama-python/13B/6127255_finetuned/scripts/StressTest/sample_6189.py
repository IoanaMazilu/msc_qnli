save_days_premise = 30
save_days_hypothesis = 80
pay_per_day = 125

# the hypothesis refers to the number of days Lexi needed to save and the pay per day, both mentioned in the premise
if save_days_hypothesis < save_days_premise:
    # check if the estimate of'save_days_hypothesis' contradicts the number of save days in the premise
    label = "contradiction"
elif pay_per_day!= 125:
    # check if the pay per day in the hypothesis contradicts the pay per day reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
