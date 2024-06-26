salary_premise = 75000
salary_hypothesis = 45000
commission_premise = 0.35
commission_hypothesis = 0.15

# the hypothesis refers to the salary and commission mentioned in the premise
if salary_hypothesis <= salary_premise:
    # check if the estimate of'salary_hypothesis' contradicts the salary in the premise
    label = "contradiction"
elif commission_hypothesis >= commission_premise:
    # check if the estimate of 'commission_hypothesis' contradicts the commission in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
