average_salary_premise = 4000
average_salary_hypothesis = 5000

# the hypothesis refers to the average salary mentioned in the premise
if average_salary_premise >= average_salary_hypothesis:
    # check if the estimate of 'average_salary_hypothesis' contradicts the average salary in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
