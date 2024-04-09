save_days_premise = 30
save_days_hypothesis = 30
pay_per_day_premise = 125
pay_per_day_hypothesis = 125

# the hypothesis refers to the number of days Lexi needed to save for a vacation and the daily pay, both mentioned in the premise
if save_days_hypothesis <= save_days_premise:
    # check if the hypothesis value contradicts the estimate of more than'save_days_premise'
    label = "contradiction"
elif pay_per_day_hypothesis!= pay_per_day_premise:
    # check if the daily pay in the hypothesis contradicts the daily pay reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days to save
    # any number of days greater than'save_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
