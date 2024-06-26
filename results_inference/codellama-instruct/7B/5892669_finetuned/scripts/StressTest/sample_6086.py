work_days_premise = 20
work_days_hypothesis = 30

# the hypothesis refers to the number of days Ram and Shyam can do a piece of work together, mentioned in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
