# Premise: $500,000 will be the limit on executive salaries at companies receiving tax dollars, President Obama says.
# Hypothesis: Pay for executives at companies that take bailout money capped at $500,000.
# Golden Label: entailment

exec_salary_limit_premise = 500000
exec_salary_limit_hypothesis = 500000

# the hypothesis mentions the salary limit of executives at companies that receive bailout money
# this limit is also mentioned in the premise
if exec_salary_limit_hypothesis != exec_salary_limit_premise:
    # check if the salary limit in the hypothesis contradicts the salary limit mentioned in the premise
    label = "contradiction"
else:
    # if the salary limit in the hypothesis does not contradict the salary limit in the premise, we can infer entailment
    label = "entailment"

print(label)

