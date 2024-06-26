salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis refers to Mary's monthly salary mentioned in the premise
if salary_premise >= salary_hypothesis:
    # check if the salary in the premise contradicts the estimate of less than'salary_hypothesis'
    label = "contradiction"
else:
    # if the salary in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)