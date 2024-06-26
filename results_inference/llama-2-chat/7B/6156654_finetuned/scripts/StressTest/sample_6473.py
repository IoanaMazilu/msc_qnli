average_salary_premise = 4000
average_salary_hypothesis = 4000

# the hypothesis mentions the average salary of Raj, Roshan and Thomas, which is also mentioned in the premise
if average_salary_hypothesis!= average_salary_premise:
    # check if the average salary in the hypothesis contradicts the average salary in the premise
    label = "contradiction"
else:
    # if the average salary in the hypothesis does not contradict the average salary in the premise, we can infer entailment
    label = "entailment"

print(label)
