mary_salary_premise = 1200
mary_salary_hypothesis = 3200

# the hypothesis refers to Mary's salary mentioned in the premise
if mary_salary_hypothesis!= mary_salary_premise:
    # check if the salary in the hypothesis contradicts the salary reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)