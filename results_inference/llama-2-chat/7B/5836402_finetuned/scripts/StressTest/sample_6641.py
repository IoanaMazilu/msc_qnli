ram_krish_work_days_premise = 40
ram_krish_work_days_hypothesis = 40

# the hypothesis refers to the number of days Bhim will take to complete the work, which is also mentioned in the premise
if ram_krish_work_days_hypothesis <= ram_krish_work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ram_krish_work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Bhim will take
    # any number of days greater than 'ram_krish_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
