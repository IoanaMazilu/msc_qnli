salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis refers to Mary's salary mentioned in the premise
if salary_premise >= salary_hypothesis:
    # check if the salary in the premise contradicts the estimate of 'less than salary_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
