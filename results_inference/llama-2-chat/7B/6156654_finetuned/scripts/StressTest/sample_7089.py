mary_salary_premise = 1200
mary_salary_hypothesis = 3200

# the hypothesis refers to Mary's salary, which is also mentioned in the premise
if mary_salary_premise >= mary_salary_hypothesis:
    # check if the premise contradicts the hypothesis
    label = "contradiction"
elif mary_salary_premise < mary_salary_hypothesis:
    # if the premise salary is less than the hypothesis salary, it is consistent with the hypothesis
    label = "entailment"
else:
    # if the premise and hypothesis salaries are equal, it is neutral
    label = "neutral"

print(label)
