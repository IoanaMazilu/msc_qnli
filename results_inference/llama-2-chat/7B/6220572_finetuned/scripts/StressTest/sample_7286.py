job_salary_premise = 75000
job_salary_hypothesis = 75000
commission_rate_hypothesis = 55

# the hypothesis talks about the salary and commission rate of John's previous and new jobs, referenced also in the premise
if job_salary_hypothesis!= job_salary_premise:
    # check if the salary in the hypothesis contradicts the salary reported in the premise
    label = "contradiction"
elif commission_rate_hypothesis!= 55:
    # check if the commission rate in the hypothesis contradicts the commission rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
