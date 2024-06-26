mary_salary_premise = 1200
mary_salary_hypothesis = 3200

# the hypothesis talks about Mary's monthly salary, which is also mentioned in the premise
if mary_salary_hypothesis!= mary_salary_premise:
    # check if the salary in the hypothesis contradicts the salary reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
