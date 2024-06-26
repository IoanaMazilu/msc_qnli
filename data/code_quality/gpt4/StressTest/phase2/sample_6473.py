average_salary_premise = 4000
average_salary_hypothesis = 4000

# the hypothesis states the same information as the premise about the average salary of Raj, Roshan, and Thomas
if average_salary_hypothesis != average_salary_premise:
    # check if the average salary in the hypothesis contradicts the one mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
