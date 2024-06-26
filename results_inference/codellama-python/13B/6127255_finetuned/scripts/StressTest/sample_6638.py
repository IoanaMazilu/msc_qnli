ram_krish_bhim_work_days_premise = 30
ram_krish_bhim_work_days_hypothesis = 50

# the hypothesis refers to the number of days Ram, Krish and Bhim can complete a work, mentioned in the premise
if ram_krish_bhim_work_days_hypothesis!= ram_krish_bhim_work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
