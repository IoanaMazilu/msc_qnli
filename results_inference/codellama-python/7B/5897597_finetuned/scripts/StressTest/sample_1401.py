sreedhar_work_days_premise = 75
sreedhar_work_days_hypothesis = 25

# the hypothesis refers to the number of days Sreedhar can do the work alone, mentioned in the premise
if sreedhar_work_days_hypothesis >= sreedhar_work_days_premise:
    # check if the estimate of'sreedhar_work_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
