days_needed_premise = 80
days_needed_hypothesis = 30
salary_per_day_premise = 125
salary_per_day_hypothesis = 125

# the hypothesis refers to the number of days needed to save for a vacation and the salary per day at the job, both mentioned in the premise
if days_needed_hypothesis > days_needed_premise:
    # check if the estimate of 'days_needed_hypothesis' contradicts the number of days needed to save for a vacation in the premise
    label = "contradiction"
elif salary_per_day_hypothesis!= salary_per_day_premise:
    # check if the salary per day in the hypothesis contradicts the salary per day reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
