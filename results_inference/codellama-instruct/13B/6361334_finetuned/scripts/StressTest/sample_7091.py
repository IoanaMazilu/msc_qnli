monthly_salary_premise = 1200
monthly_salary_hypothesis = 3200

# the hypothesis refers to the monthly salary mentioned in the premise
if monthly_salary_hypothesis <= monthly_salary_premise:
    # check if the estimate of'monthly_salary_hypothesis' contradicts the monthly salary in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
