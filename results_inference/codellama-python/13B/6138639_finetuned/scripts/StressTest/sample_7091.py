salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis refers to Mary's monthly salary mentioned in the premise
if salary_hypothesis!= salary_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
