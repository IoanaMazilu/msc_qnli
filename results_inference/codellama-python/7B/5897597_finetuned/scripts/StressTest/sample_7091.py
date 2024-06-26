salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis refers to Mary's salary mentioned in the premise
if salary_premise!= salary_hypothesis:
    # check if the salary in the hypothesis contradicts the salary reported in the premise
    label = "contradiction"
else:
    # if the salary in the hypothesis does not contradict the salary in the premise, we can infer entailment
    label = "entailment"

print(label)
