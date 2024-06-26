ram_krish_work_days_premise = 40
ram_krish_work_days_hypothesis = 40

# the hypothesis refers to the number of days Ram and Krish can complete a work, mentioned in the premise
if ram_krish_work_days_hypothesis <= ram_krish_work_days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
