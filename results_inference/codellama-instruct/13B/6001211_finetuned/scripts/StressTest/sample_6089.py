total_work_days_premise = 12 + 10
total_work_days_hypothesis = 72

# the hypothesis refers to the total number of days they worked together, mentioned in the premise
if total_work_days_hypothesis!= total_work_days_premise:
    # check if the total number of days worked together in the hypothesis contradicts the total number of days worked together reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
