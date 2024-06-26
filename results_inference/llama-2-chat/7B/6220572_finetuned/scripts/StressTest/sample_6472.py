average_salary_premise = 4000
average_salary_hypothesis = 4000

# the hypothesis refers to the average salary of Raj, Roshan and Thomas mentioned in the premise
if average_salary_hypothesis!= average_salary_premise:
    # check if the average salary in the hypothesis contradicts the average salary reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
