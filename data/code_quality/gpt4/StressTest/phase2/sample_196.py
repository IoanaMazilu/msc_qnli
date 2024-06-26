work_days_renu_premise = 5
work_days_renu_hypothesis = 6
work_days_renu_suma_premise = 5
work_days_renu_suma_hypothesis = 5

# the hypothesis refers to the number of days Renu and Renu+Suma can complete work, mentioned in the premise
if work_days_renu_hypothesis <= work_days_renu_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_renu_premise' days
    label = "contradiction"
elif work_days_renu_suma_hypothesis != work_days_renu_suma_premise:
    # check if the number of days Renu+Suma can complete work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate (more than 'work_days_renu_premise' days) for the number of days Renu can complete the work
    # any number of days more than 'work_days_renu_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
