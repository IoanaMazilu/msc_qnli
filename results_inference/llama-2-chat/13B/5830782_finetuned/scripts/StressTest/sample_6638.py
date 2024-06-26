work_days_premise = 30
work_days_hypothesis = 50

# the hypothesis refers to the number of days Ram, Krish and Bhim can complete a work, also mentioned in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)