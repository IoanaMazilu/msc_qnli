mary_salary_premise = 1200
mary_salary_hypothesis = 3200

# the hypothesis refers to the monthly salary of Mary mentioned in the premise
if mary_salary_premise >= mary_salary_hypothesis:
    # check if the salary of Mary in the premise contradicts the hypothesis of less than'mary_salary_hypothesis'
    label = "contradiction"
else:
    # if the premise salary is less than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
