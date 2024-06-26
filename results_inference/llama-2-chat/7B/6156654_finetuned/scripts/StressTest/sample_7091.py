mary_salary_premise = 1200
mary_salary_hypothesis = 3200

# the hypothesis talks about Mary's salary, which is also mentioned in the premise
if mary_salary_hypothesis!= mary_salary_premise:
    # check if the salary in the hypothesis contradicts the salary in the premise
    label = "contradiction"
else:
    # if the salary in the hypothesis matches the salary in the premise, we can infer entailment
    label = "entailment"

print(label)
