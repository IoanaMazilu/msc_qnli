save_days_premise = 30
save_days_hypothesis = 80
pay_per_day = 125

# the hypothesis refers to the number of days Lexi needed to save for a vacation, as mentioned in the premise
if save_days_premise >= save_days_hypothesis:
    # check if the number of days in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
