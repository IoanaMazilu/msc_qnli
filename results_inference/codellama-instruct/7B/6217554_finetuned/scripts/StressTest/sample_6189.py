days_premise = 30
days_hypothesis = 80
salary_per_day_premise = 125
salary_per_day_hypothesis = 125

# the hypothesis refers to the number of days and salary per day mentioned in the premise
if days_hypothesis <= days_premise:
    # check if the estimate of 'days_hypothesis' contradicts the number of days needed in the premise
    label = "contradiction"
elif salary_per_day_hypothesis!= salary_per_day_premise:
    # check if the salary per day in the hypothesis contradicts the salary per day reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
