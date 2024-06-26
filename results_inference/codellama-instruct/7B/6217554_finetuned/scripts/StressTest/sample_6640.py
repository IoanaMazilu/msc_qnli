ram_krish_work_days_premise = 20
ram_krish_work_days_hypothesis = 40

# the hypothesis refers to the number of days needed for the same work by Ram and Krish, mentioned in the premise
if ram_krish_work_days_hypothesis <= ram_krish_work_days_premise:
    # check if the number of days needed by Ram and Krish in the hypothesis contradicts the estimate of more than 'ram_krish_work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days needed by Ram and Krish
    # any number of days greater than 'ram_krish_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
