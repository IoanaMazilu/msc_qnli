work_days_premise = 11
work_days_hypothesis = 81

# the hypothesis refers to the number of days Mary can do a piece of work, which is also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
