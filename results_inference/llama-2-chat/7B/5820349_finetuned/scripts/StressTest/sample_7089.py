mary_salary_premise = 1200
mary_salary_hypothesis = 3200

# the hypothesis refers to Mary's monthly salary mentioned in the premise
if mary_salary_premise >= mary_salary_hypothesis:
    # check if the estimate of'mary_salary_hypothesis' contradicts the salary of Mary in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
