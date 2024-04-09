work_days_premise = 11
work_days_hypothesis = 81

# the hypothesis refers to the number of days Mary can do a piece of work, mentioned in the premise
if work_days_premise >= work_days_hypothesis:
    # check if the estimate of 'work_days_premise' contradicts the number of days in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
