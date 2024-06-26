ram_krish_bhim_work_days_premise = 30
ram_krish_bhim_work_days_hypothesis = 50

# the hypothesis refers to the number of days Ram, Krish and Bhim can complete a work, mentioned in the premise
if ram_krish_bhim_work_days_hypothesis < ram_krish_bhim_work_days_premise:
    # check if the estimate of 'ram_krish_bhim_work_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
# 