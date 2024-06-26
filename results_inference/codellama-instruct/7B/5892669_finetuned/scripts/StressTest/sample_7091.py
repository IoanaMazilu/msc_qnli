salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis refers to the monthly salary of Mary mentioned in the premise
if salary_hypothesis!= salary_premise:
    # check if the monthly salary in the hypothesis contradicts the monthly salary reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
