albert_work_days_premise = 20
albert_work_days_hypothesis = 20
rose_work_days_premise = 30
rose_work_days_hypothesis = 30

# the hypothesis refers to the number of days Albert and Rose need to complete the same work as mentioned in the premise
if albert_work_days_hypothesis < albert_work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days Albert needs to complete the work according to the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the number of days Rose needs to complete the work according to the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
