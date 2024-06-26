'salary_mary_premise' and'salary_mary_hypothesis'

salary_mary_premise = 1200
salary_mary_hypothesis = 3200

# the hypothesis refers to Mary's monthly salary, which is also mentioned in the premise

if salary_mary_hypothesis!= salary_mary_premise:
    # check if the salary in the hypothesis contradicts the salary reported in the premise
    label = "contradiction"
else:
    # if the salary in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)

