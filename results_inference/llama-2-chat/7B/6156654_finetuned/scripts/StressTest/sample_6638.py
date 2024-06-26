work_days_premise = 30
work_days_hypothesis = 50

# the hypothesis refers to the time it takes for Ram, Krish and Bhim to complete a work, which is also mentioned in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days in the premise
    label = "contradiction"
else:
    # if the number of work days in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
