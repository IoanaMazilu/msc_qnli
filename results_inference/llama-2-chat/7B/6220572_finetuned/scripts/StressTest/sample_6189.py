days_premise = 30
days_hypothesis = 80
salary_premise = 125
salary_hypothesis = 125

# the hypothesis refers to the number of days and salary needed for a vacation mentioned in the premise
if days_hypothesis >= days_premise:
    # check if the estimate of 'days_hypothesis' contradicts the number of days needed in the premise
    label = "contradiction"
elif salary_hypothesis!= salary_premise:
    # check if the salary in the hypothesis contradicts the salary reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
